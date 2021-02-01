from bs4 import BeautifulSoup
import requests
import csv
	

def get_html(url):
	r = requests.get(url)
	return r.text

def clean_num(s):
	r = s.split(' ')[0]
	r = r.replace(',', '')
	return r


def write_csv(data):
	with open('test.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow((data['name'], data['url'], data['rating']))


def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	popular = soup.find_all('section')[1]
	plugins = popular.find_all('article')
	for plugin in plugins:
		name = plugin.find('h3').text
		url = plugin.find('h3').find('a').get('href')
		r = plugin.find('span', class_='rating-count').find('a').text
		rating = clean_num(r)

		data = {'name': name,
				'url': url,
				'rating': rating}

		write_csv(data)


def main():
	url = 'https://wordpress.org/plugins/'
	print(get_data(get_html(url)))


if __name__ == '__main__':
	main()