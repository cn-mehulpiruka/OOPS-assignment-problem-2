class node:
	def __init__(self):
		self.value=-1
		self.next=None
	@classmethod
	def create_new_node(cls,value_,obj_=None):
		n=node()
		n.value=value_
		n.next=obj_
		# print(n.next)
		return n

class linkedlist:
	head=None

	@classmethod
	def insert_begin(cls,value_):
		if linkedlist.head==None:
			linkedlist.head=node.create_new_node(value_)
			return
		n=node.create_new_node(value_,linkedlist.head)
		linkedlist.head=n
		# print(linkedlist.head)
	@classmethod
	def insert_end(cls,value_):
		if linkedlist.head==None:
			linkedlist.head=node.create_new_node(value_)
			return
		temp=linkedlist.head
		while temp.next!=None:
			temp=temp.next
		n=node.create_new_node(value_)
		temp.next=n

	@classmethod
	def insert_at_a_pos(cls,pos,value_):
		if linkedlist.head==None:
			linkedlist.head=node.create_new_node(value_)
		if pos==0:
			linkedlist.insert_begin(value_)
			return
		temp=linkedlist.head
		cnt=1
		while temp!=None and cnt<pos-1:
			temp=temp.next
			cnt+=1
			# print(cnt)
		if cnt+1==pos or temp!=None:
			n=node.create_new_node(value_,temp.next)
			temp.next=n
		else:
			print ("Cannot Insert...!!!! Index out of Bound")
	

	@classmethod
	def delete_begin(cls):
		if linkedlist.head==None:
			print("Sorry got nothing to delete")
			return

		print("Poped element at begin:",linkedlist.head.value)
		linkedlist.head=linkedlist.head.next
		# pass
	@classmethod
	def delete_end(cls):
		if linkedlist.head==None:
			print("Sorry got nothing to delete")
			return

		temp=linkedlist.head
		while temp.next.next!=None:
			temp=temp.next
		print("Poped element at end: ",temp.next.value)
		temp.next=None
		
	@classmethod
	def delete_at_a_pos(cls,pos):
		if linkedlist.head==None:
			print("Sorry got nothing to delete")
			return
		if pos==0:
			linkedlist.delete_begin()
			return
		temp=linkedlist.head
		cnt=1
		while temp.next!=None and cnt<pos-1:
			temp=temp.next
			cnt+=1
		if temp.next!=None:
			# print("del",temp.next.value)
			if temp.next.next==None:
				linkedlist.delete_end()
				return
			else:
				del_node=temp.next
				print("Poped element at pos",pos,"is ",temp.next.value)
				temp.next=temp.next.next

		else:
			print("Cannot delete..!!! Index out of bound")
			










	@classmethod
	def display(cls):
		if linkedlist.head==None:
			print("Hey,!! Got nothing to print")
		temp=linkedlist.head
		while temp!=None:
			print(temp.value)
			temp=temp.next


ll=linkedlist()

linkedlist.insert_begin("#")
linkedlist.insert_begin("$")
linkedlist.insert_begin(9)

linkedlist.insert_end(39)
linkedlist.insert_begin("%")

linkedlist.insert_end(49)
linkedlist.insert_end(59)
linkedlist.insert_at_a_pos(7,30)


linkedlist.display()
print("========="*4,"After insert","========="*4)
linkedlist.delete_begin()
linkedlist.delete_end()
linkedlist.delete_at_a_pos(1)

linkedlist.display()

# print(linkedlist.__dict__)
