import requests
import csv


def get_html(url):
	r = requests.get(url)
	return r.text

def write_csv(data):
	with open('live.csv', 'a') as f:
		order = ['name', 'url', 'description', 'trafic']
		writer = csv.DictWriter(f, fieldnames=order)
		writer.writerow(data)

def main():
	for i in range(0, 6428):
		url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(str(i))
		response = get_html(url)
		data = response.strip().split('\n')[1:]
		# print(data)

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
		

if __name__ == '__main__':
	main()
