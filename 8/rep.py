from bs4 import BeautifulSoup
import re 



def main():
	file = open('stopgame.txt', 'r')
	soup = BeautifulSoup(file, 'lxml').decode('utf-8')
	print(soup)



if __name__ == '__main__':
	main()