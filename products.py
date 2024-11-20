import os #operating system


products = []
if os.path.isfile('products.csv'):
	print('yeah!找到檔案了!')
	with open('products.csv','r',encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name,price = line.strip().split(',') #split切割完結果是清單
			products.append([name,price])
	print(products)
else:
	print('找不到檔案...')

#讀取檔案


#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name,price])
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0],'的價格是',p[1],'元')

#寫入檔案
with open('products.csv','w',encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')