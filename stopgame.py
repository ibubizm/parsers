from bs4 import BeautifulSoup
import requests
import csv

def get_html(url):
	r = requests.get(url)
	return r.text

def write_csv(data_dict):
	with open('stopgame.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow((data_dict['name'], data_dict['url'], data_dict['data'], data_dict['comments']))


def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	items = soup.find('div', class_='tiles tiles-details').find_all('div', class_='item article-summary')
	# print(items)
	for item in items:
		try:
			name = item.find('div', class_='caption caption-bold').text
		except:
			name = 'non'
		try:
			url = item.find('a').get('href')
			url = 'https://stopgame.ru' + url
		except:
			url = ''
		try:
			data = item.find('span', class_='info-item timestamp').text
		except:
			data = ''
		try:
			comments = item.find('span', class_='info-item comments').text
		except:
			comments = ''

		data_dict = {'name': name, 'url': url, 'data': data, 'comments': comments}
		print(data_dict)
		write_csv(data_dict)



def main():
	pattern = 'https://stopgame.ru/news/all/p{}'
	for i in range(1, 10):
		url = pattern.format(str(i))
		get_data(get_html((url)))
		print(url)


if __name__ == '__main__':
	main()