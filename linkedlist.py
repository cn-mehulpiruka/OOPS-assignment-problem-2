class node:
	def __init__(self,data):
		self.data = data
		self.next = None
class Linkedlist:
	def __init__(self):
		self.head = None
	def insertfront(self,new_data):
		new_node = node(new_data)
		new_node.next = self.head
		self.head = new_node
	def insertend(self,new_data):
		new_node = node(new_data)
		temp = self.head
		while temp.next is not None:
			temp = temp.next
		temp.next = new_node
	def insertatpos(self,newNode,index):
		temp = self.head
		count = 0
		while True:
			if count==index:
				prev.next = newNode
				newNode.next = temp
				break
			prev = temp
			temp = temp.next
			count += 1		
	def search(self,d):
		temp = self.head
		while temp is not None:
			if(temp.data == d):
				return True
			temp = temp.next
		return False	
	def deletefirst(self):
		temp = self.head
		temp1 = self.head.next
		if(temp.data):
			self.head = temp1
			del(temp)
	def deleteend(self):
		lastnode = self.head
		while lastnode.next is not None:
			prevnode = lastnode
			lastnode = lastnode.next
		prevnode.next = None
	def deleteatpos(self,d):
		val = self.head
		if(val is not None):
			if(val.data == d):
				self.head = val.next
				val = None
				return
		while val is not None:
			if(val.data == d):
				break
			previnode = val
			val = val.next
		if(val == None):
			return
		previnode.next = val.next
		val = None
	def deletepos(self, pos):
		currentNode = self.head
		countt = 0
		while True:
			if countt == pos:
				prevNode.next = currentNode.next
				currentNode.next = None
				break
			prevNode = currentNode
			currentNode = currentNode.next
			countt += 1
	def printlist(self):
		temp = self.head
		while temp is not None:
			print(temp.data)
			temp = temp.next
llist = Linkedlist()
llist.head = node(1)
second = node(2)
third = node(3)
fourth = node(4)
llist.head.data = 10
llist.head.next = second;
second.data = 20
second.next = third;
third.data = 40
third.next = fourth;
fourth.data = 70
fourth.next = None
llist.printlist()
llist.insertfront(input("enter data to insert at first:"))
llist.printlist()
llist.insertend(input("enter data to insert at end"))
llist.printlist()
print("insert at position")
fifth = node(15)
llist.insertatpos(fifth, 1)
llist.printlist()
print("item found")
if llist.search(10):
	print("yes")
else:
	print("no")
llist.deletefirst()
print("first node deleted")
llist.printlist()
llist.deleteend()
print("last node deleted")
llist.printlist()
print("delition by data")
llist.deleteatpos(20)
llist.printlist()
print("delete at position")
llist.deletepos(3)
llist.printlist()












