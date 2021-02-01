import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
	user_agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
	r = requests.get(url)
	return r.text

def write_csv(data):
	with open('new.csv', 'a') as f:
		order = []
		writer = csv.DictWriter(f, fieldnames=order)
		writer.writerow(data)

def get_artic(html):
	soup = BeautifulSoup(html, 'lxml')
	ts = soup.find('div', class_='themify_builder_row module_row clearfix module_row_3 themify_builder_2364_row module_row_2364-3').find_all('article')
	return ts


def get_data(ts):
	for t in ts:
		try:
			since = t.find('div', class_='author-details').text.strip()
			print(since)
		except:
			print('ni')


def main():
	url = 'https://catertrax.com/why-catertrax/traxers/page/6/?themify_builder_infinite_scroll=yes'
	get_data(get_html(url))


if __name__ == '__main__':
	main()