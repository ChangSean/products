import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	if os.path.isfile(filename):
		print('yeah!找到檔案了!')
		with open(filename,'r',encoding='utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue #繼續
				name,price = line.strip().split(',') #split切割完結果是清單
				products.append([name,price])
		print(products)
	else:
		print('找不到檔案...')
	return products


#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		price = int(price)
		products.append([name,price])
	print(products)
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0],'的價格是',p[1],'元')

#寫入檔案
def write_file(filename,products):
	with open(filename,'w',encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv',products)