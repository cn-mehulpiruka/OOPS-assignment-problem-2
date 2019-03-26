class linkedlist:
	def __init__(self):
		pass
	def create_newnode(self,value_):
		self.value=value_
		self.next=None
		return self
	def insert_begin(self,value_):
		if self==None:
			self=create_newnode(value_)
			print("head_",self)
			return self
		new_node=linkedlist()
		new_node=new_node.create_newnode(value_)
		print("head_",self.value,"new_node",new_node.value)
		# new_node.create_newnode(new_node.value,head_)
		new_node.next=self
		self=new_node
		print("head_",self.value,"new_node",self.value)
		return self
	def insert_end(self,value_,head_):
		if head_==None:
			head_=linkedlist()
			print("head_",head_)
			return head_
		temp=head_
		while temp.next!=None:
			temp=temp.next
		new_node=create_newnode(value_)
		# temp.create_newnode(new_node.value,new_node)

	def display(self):
		temp=self
		print("nxe",temp.next)
		while temp.next!=None:
			print("temp",temp)
			print(temp.value)
			# print(temp.next)
			temp=temp.next

if __name__=="__main__":
	head_=linkedlist()
	# print(head_)
	# obj.display(obj)
	head_=head_.insert_begin(15)
	# print("head_",head_)
	head_=head_.insert_begin(25)
	# head_.display()
	# linkedlist().insert_end(25,head_)
	# linkedlist().display(head_)


	


