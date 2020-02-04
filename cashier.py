def main():
	done = True
	listofitems = []
	itemsdic = {'item':'','price':0.0,'quan':0}
	totalprice = 0
	while done:
		item = input("Item (enter \"done\" when finished):")
		if item == "done" or item == "Done":
			done = False
			pass
		else:
			itemsdic['item'] = item
			price = float(input("Price:"))
			itemsdic['price']= price
			quan = int(input("Quantity"))
			itemsdic['quan'] = quan
			listofitems.append(itemsdic)
			print("-------------------")
		pass
	print("-------------------")
	print("receipt")
	print("-------------------")
	for item in listofitems:
		totalprice = totalprice + (item['price']* item['quan'])
		print(str(item['quan']) + " " + item['item']+" " +str(item['price']*item['quan'])+"KD")
	print("-------------------")
	print("Total Price: "+str(totalprice)+"KD")

if __name__ == '__main__':
	main()
