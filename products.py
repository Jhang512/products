import os # opeartion system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f: # Add read file
		for line in f:
			if 'Item,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# User input start
def user_input(products):
	while True:
		item = input('Please in put product\'s name: ')
		if item == 'q':
			break
		price = input('Please in put product\'s price: ')
		price = int(price)
	#	p = [item, price] # simplified on line 15
	#	p.append(item) # simplified on line 10
	#	p.append(price) # simplified on line 10
		products.append([item, price])
	print (products)
	return products

# Print all the records
def print_products(products):
	for p in products:
		print(p[0],'\'s price is ', p[1])

# Write to a new file
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('Item,Price' + '\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main(filename):
	if os.path.isfile(filename):
		print('File exist.')
		products = read_file(filename)
		print (products)
	else:
		print('File not exist.')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main('products.csv')