class linkedlist:
	def __init__(self,value_=0):
		self.value=value_
		self.next=None

	def setvalue(self,value_,obj_):
		self.value=value_
		self.next=obj_
	def insert_begin(self,value_,start_obj_):
		temp=start_obj_
		new_node=linkedlist(value_)
		new_node.setvalue(new_node.value,start_obj_)
		return new_node
	# def insert_end(self,value_,start_obj_):
	def display(self,start_obj_):
		temp=start_obj_
		while temp!=None:
			# print("temp",temp)
			print(temp.value)
			# print(temp.next)
			temp=temp.next

obj=linkedlist(5)
obj.display(obj)
obj=obj.insert_begin(15,obj)
obj.display(obj)



	


