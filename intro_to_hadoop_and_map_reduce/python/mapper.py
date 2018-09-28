def mapper(lines):
	key = None
	newKey = None
	newValue = 0
	value = 0
	details = None

	for line in sys.stdin:
		data = line.strip().split("\t")

		if data.lenght != 3:
			print("wrong input: %s",data)
		else:
			newkey,newvalue,details = data
			print (data)

			if 	key == newKey:
				value = value+newValue
			else:
				print (key,value)
				key = newKey

	def main():
		lines = """Lucia\t20\t"Bella"\t"""
		mapper(lines)



