from bs4 import BeautifulSoup
import requests
import csv
import re
from peewee import *

db = PostgresqlDatabase(database='coin', user='postgres', password='123', host='localhost')


class Coin(Model):
	name = CharField()
	price = CharField()


	class Meta:
		database = db


def get_html(url):
	r = requests.get(url)
	return r.text


def write_csv(data):
	with open('new.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow((data['name'], data['price']))

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	items = soup.find('tbody').find_all('tr', class_='cmc-table-row')
	for item in items:
		try:
			name = item.find('a').text
		except:
			name = 'non'
		try:
			price = item.find('td', class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price').text
		except:
			price = 'non'

		data = {'name': name, 'price': price}
		write_csv(data)



def main():
	db.connect()
	db.create_tables([Coin])

	with open('new.csv', 'r') as f:
		order = ['name', 'price']
		reader = csv.DictReader(f, fieldnames=order)

		coins = list(reader)

		with db.atomic():
			for row in coins:
				Coin.create(**row)




	url ='https://coinmarketcap.com/'
	while True:
		get_data(get_html(url))

		soup = BeautifulSoup(get_html(url), 'lxml')
		try:
			pattern = 'Next'
			url = 'https://coinmarketcap.com' + soup.find('div', class_='va78v0-0 bOJMMo cmc-table-listing__pagination-button-group cmc-button-group').find('a', text=re.compile(pattern)).get('href')
			print(url)
		except:
			break


if __name__ == '__main__':
	main()