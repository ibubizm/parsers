import requests 
import csv
from multiprocessing import Pool

def get_html(url):
	r = requests.get(url)
	return r.text

def write_csv(data):
	with open('web.csv', 'a') as f:
		order = ['name', 'url', 'description', 'trafic' ]
		writer = csv.DictWriter(f, fieldnames=order)
		writer.writerow(data)


def get_data(text):
	data = text.strip().split('\n')[1:]
	for row in data:
			colums = row.strip().split('\t')
			# print(colums)
			name = colums[0]
			url = colums[1]
			description = colums[3]
			trafic = colums[4]
			
			data = {'name': name,
					'url':url,
					'description': description,
					'trafic': trafic}
			write_csv(data)


def make_all(url):
	# 6787
	text = get_html(url)
	get_data(text)


def main():
	url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
	urls = [url.format(str(i)) for i in range(1, 67)]
	
	with Pool(20) as p:
		p.map(make_all, urls)

if __name__ == '__main__':
	main()