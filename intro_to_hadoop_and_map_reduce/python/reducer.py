import io

def mapper(inputs):
	clean_data = {}
	for line in inputs:
		data = line.strip().split("\t")
		if len(data) != 6:
			continue
		clean_data += data[2],data[4]
	return clean_data


def reducer(data):
	total = 0
	oldCity = None

	for line in data:
		city,price = data
		if (oldCity and oldCity != city):
			print(oldCity, total)
			total = 0
		oldCity = city
		total += float(price)
	if oldCity != None:
		print(oldCity, total)

if __name__ == '__main__':
	inputs = """2013-10-09\t13:22\tMiami\tBoots\t99\tVisa
		2013-10-09\t13:22\tMiami\tBoots\t28\tMasterCard
		2013-10-09\t13:22\tNew York\tDVD\t9.50\tMasterCard
		2013-10-09 13:22:59 I/O Error
		^d8x28orz28zoijzu1z1zp1OHH3du3ixwcz114<f
		1\t2\t3"""
	inputs = io.StringIO(inputs)
	data = mapper(inputs)
	reducer(data)
