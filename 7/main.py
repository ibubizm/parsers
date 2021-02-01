import csv


def write_csv(data):
	with open('names.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([data['name'], data['lastname']])


def write_csv(data):
	with open('names.csv', 'a') as f:
		order = ['name', 'lastname']
		writer = csv.writer(f, fieldname=order)
		writer.writerow(data)





def main():
	d = {'name': 'ernest', 'lastname': 'ibubizm'}
	d1 = {'name': 'any', 'lastname': 'none'}
	d2 = {'name': 'ksu', 'lastname': 'none'}

	l = [d, d1, d2]

	for i in l:
		write_csv(i)


if __name__ == '__main__':
	main()