def main():
	done = True
	listofitems = []
	itemsdic = {'name':'','price':0.0,'quantity':0}
	totalprice = 0
	while done:
		item = input("Item (enter \"done\" when finished):")
		if item == "done" or item == "Done":
			done = False
			pass
		else:
			newdic = itemsdic.copy()
			newdic['name'] = item
			price = float(input("Price:"))
			newdic['price']= price
			quan = int(input("Quantity:"))
			newdic['quantity'] = quan
			listofitems.append(newdic)
		pass
	print("")
	print("")
	print("-------------------")
	print("receipt")
	print("-------------------")
	for item in listofitems:
		totalprice = float(totalprice + (item['price']* item['quantity']))
		print(str(item['quantity']) + " " + item['name']+" " +str((item['price']*item['quantity']))+"KD")
	print("-------------------")
	print("Total Price: "+str(totalprice )+"KD")

if __name__ == '__main__':
	main()
