from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
	r = requests.get(url)
	if r.ok:
		return r.text.encode('latin-1').decode('utf-8')
	else:
		print(r.status_code)


def write_csv(data):
	with open('auto.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([data['title'], data['year'], data['price'], data['url']])
	

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	bodys = soup.find('div', class_='listing').find_all('div', class_='listing-item-body')

	for body in bodys:
		try:
			title = body.find('div', class_='listing-item-title').find('h4').find('a').text.strip()
		except:
			title = 'не найдено'
		try:
			year = body.find('div', class_='listing-item-desc').find('span').text
		except:
			year = 'не найдено'
		try:
			price = body.find('div', class_='listing-item-price').find('small').text.replace(' ', '') + '$'
		except:
			price = 'не найдено'
		try:
			url = body.find('div', class_='listing-item-title').find('h4').find('a').get('href')
		except:
			url = ''


		data = {'title': title, 'year': year, 'price': price, 'url': url}
		# print(data)

		write_csv(data)


def main():
	pattern = 'https://cars.av.by/volkswagen/passat-cc/page/{}'
	for i in range(1, 6):
		url = pattern.format(str(i))
		print(url)

		get_data(get_html(url))

if __name__ == '__main__':
	main()