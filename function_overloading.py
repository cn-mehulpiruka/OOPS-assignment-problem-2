class wrk_name:
	val=5
	def __init__(self):
		self.val=10
	def change_val(self):
		# print(self)
		self.val=20
	def switch_obj(self,obj):
		temp=self
		print("self",self)
		print("temp",temp)
		print("obj",obj,"\n")
		self=obj
		obj=temp
	def __add__(self,obj1):
		print(self)
		return self.val+obj1.val
print("intialising obj")
obj=wrk_name()
print("obj",obj.val)
print("obj",obj)

# print(obj)
print("Changing obj")

obj.change_val()
print("obj",obj.val)
print("intialising obj1")

obj1=wrk_name()
print("obj1",obj1.val)
print("obj1",obj1)

print("Switching obj")

obj1.switch_obj(obj)
print("obj",obj)
print("obj1",obj1)
print("obj",obj.val)
print("obj1",obj1.val)

print(obj1+obj)
print(wrk_name.__dict__)
print(obj.__dict__)
