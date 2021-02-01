from peewee import *
import csv


db = PostgresqlDatabase(database='coin', host='localhost', user='postgres', password='123')

class Coin(Model):
	name = CharField()
	price = CharField()

	class Meta:
		database = db


def main():
	db.connect()
	db.create_tables([Coin])

	with open('new.csv', 'r') as f:
		order = ['name', 'price']
		reader = csv.DictReader(f, fieldnames=order)
		coins = list(reader)
		
		with db.atomic():
			for index in range(0, len(coins), 100):
				Coin.insert_many(coins[index:index+100]).execute()


if __name__ == '__main__':
	main()