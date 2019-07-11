import os # opeartion system

products = []

if os.path.isfile('products.csv'):
	print('File exist.')
	with open('products.csv', 'r', encoding='utf-8') as f: # Add read file
		for line in f:
			if 'Item,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('File not found.')






# User input start
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

# Print all the records
for p in products:
	print(p[0],'\'s price is ', p[1])

# Write to a new file
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Item,Price' + '\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')