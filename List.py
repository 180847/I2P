fruitlist= ["apple","orange","banana","watermelon","Dhruv","Mango","Krish"]
print(fruitlist[0])
print(fruitlist[-3])

numberlist1=[1,2,3]
numberlist2=[4,5,6]

numberlist3=numberlist1+numberlist2
print(numberlist3)

print(numberlist3*3)

print(fruitlist[:5])
print(fruitlist[1:3])

#fruitlist[5]="dumb"
#print(fruitlist)

olpymiclist=(["London",2012],["Beijing",2008],["Athens",2004])
print(olpymiclist)
print(olpymiclist[2])

inventorylist = ["sword","sheild","armour","healing potion"]
print(inventorylist)
inventorylist.insert(2,"cabbage")
print(inventorylist)

inventorylist.sort()
#alphabedical order
print(inventorylist)
print(inventorylist.count("sword"))

inventorylist.extend(fruitlist)
print (inventorylist)

fruitlist= ["apple","orange","banana","watermelon","Dhruv","Mango","Krish"]

vfruit= fruitlist.pop()
print (fruitlist)
print(vfruit)

fruitlist= ["apple","orange","banana","watermelon","Dhruv","Mango","Krish"]
fruitlist.remove("Dhruv")
print(fruitlist)

fruitlist.sort()
fruitlist.reverse()
print(fruitlist)

vindex=fruitlist.index("banana")
print(vindex)

print(len(fruitlist))

print("apple"in fruitlist)

print(max(fruitlist))
