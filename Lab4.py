from functools import reduce
import csv

with open("1.csv","r") as file:
	keys = file.readline()
	reader = csv.reader(file, delimiter=",")
	dataset = [x for x in reader]
	keys = list(keys.split(","))
	town = list(map(lambda x: x[9] == 'Москва', dataset))
	print(town.count(True))