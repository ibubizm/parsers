import csv
from peewee import *

db = PostgresqlDatabase(database='test', user='postgres', password='123', host='localhost')


class Cars(Model):
	name = CharField()
	year = CharField()
	url = TextField()
	price = CharField()

	class Meta:
		database = db



def main():

	db.connect()
	db.create_tables([Cars])


	with open('auto.csv', 'r') as f:
		order = ['name', 'year', 'price', 'url']
		reader = csv.DictReader(f, fieldnames=order)

		cars = list(reader)

		# for row in cars:
		# 	car = Cars(name=row['name'], url=row['url'], year=row['year'], price=row['price'])
		# 	car.save()

		with db.atomic():
			for row in cars:
				Cars.create(**row)


if __name__ == '__main__':
	main()