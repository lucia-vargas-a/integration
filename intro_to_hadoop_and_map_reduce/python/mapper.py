import sys

class Mapper():

	def mapper_city(): #self, lines):
		clean_data = []
		for line in inputs:
			data = line.strip().split("\t")
			if len(data) != 6:
				continue
			clean_data += data[3], data[4]
		return clean_data
