import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	return r.text

def get_page_data(response):
	if 'html' in response.headers['Content-Type']:
		html = response.text
	else:
		html = response.json()

	soup = BeautifulSoup(html, 'lxml')
	items = soup.find('h3', class_='style-scope ytd-grid-video-renderer')
	print(items)

# def get_data(html):
# 	soup = BeautifulSoup(html, 'lxml')
# 	items = soup.find('div', class_='style-scope ytd-grid-renderer')
# 	print(items)

def main():
	url = 'https://www.youtube.com/c/StopGameRuGames/videos'
	print(get_html(url))
	# print(get_page_data(get_html(url)))


if __name__ == '__main__':
	main()