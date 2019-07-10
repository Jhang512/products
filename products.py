products = []

while True:

	item = input('Please in put product\'s name: ')
	if item == 'q':
		break
	price = input('Please in put product\'s price: ')

#	p = [item, price] # simplified on line 15

#	p.append(item) # simplified on line 10
#	p.append(price) # simplified on line 10

	products.append([item, price])

print (products)

for p in products:
	print(p[0],'\'s price is ', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')