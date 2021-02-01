import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
	r = requests.get(url)
	return r.text


def write_csv(data):
	with open('new.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(())


def get_data(html):
	soup = BeautifulSoup(html, 'lxml')


def main():
	pass


if __name__ == '__main__':
	main()