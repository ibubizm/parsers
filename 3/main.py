from bs4 import BeautifulSoup
import csv
import requests

def clean_num(price):
	p = price.replace('.', '').replace('$', '')
	return p

def get_html(url):
	r = requests.get(url)
	return r.text

def write_csv(data):
	with open('coins.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([data['name'], data['url'], data['price']])


def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	items = soup.find('tbody').find_all('tr', class_='cmc-table-row')
	for item in items:
		try:
			name = item.find('div', class_='sc-1kxikfi-0 fjclfm cmc-table__column-name').text
		except:
			name = ''
		try:
			url = 'https://coinmarketcap.com' + item.find('a').get('href')
		except:
			url = ''
		try:
			price = item.find('td', class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price').text
			price = clean_num(price)
		except:
			price = ''
		

		data = {'name': name, 'url': url, 'price': price + '$'}

		write_csv(data)


def main():
	url = 'https://coinmarketcap.com/all/views/all/'
	get_data(get_html(url))


if __name__ == '__main__':
	main()