class Person:
	id=20000
	name='lokesh'
	course='dbms'
	clg="KlU"
	"""docstring for ClassName"""

	def __init__(self,id,name,course):
			self.id=id
			self.name=name
			self.course=course

	def disply(self,):
			print(f"this is{self.id}")
			print(f"this is{self.name}")
			print(f"this is{self.course}")

s1 = Person( 1234," lokesh"," PFSD")
print(s1)
s1.disply()
print(s1.clg)
