class Component(object):
	'''Abstract class'''

	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		'''Interface Method'''
		pass

class Child(Component):
	'''Concrete class'''

	def __init__(self, *args, **kwargs):
		'''Inherits from abstract class Componen'''
		Component.__init__(self, *args, **kwargs)

		'''Attribute to store the name of the child'''
		self.name = args[0] 		# Simply getting an argument from the instance of the child class. Here, the first argument will be used


	'''Implementing the abstract method'''
	def component_function(self):
		'''Print the name of the child items as an implementation'''
		print("\t{}".format(self.name))

class Composite(Component):
	'''A Concrete class which maintains the tree recursive structure'''

	def __init__(self, *args, **kwargs):
		'''Inherits from the abstract Component class'''
		Component.__init__(self, *args, **kwargs)

		'''We also need another attribute to store the name of the Composite object'''
		self.name = args[0]				# We will be using the first argument to get the name of the composite object

		'''We will need another attribute which is a list that is going to be keeping all our child items in the composite object'''
		self.children = []

	'''Following are utility methods'''
	def append_child(self, child):
		'''Used to add new child'''
		self.children.append(child)

	def remove_children(self, child):
		'''Used to remove a child item'''
		self.children.remove(child)

	'''Definition of our abstract method, component_function'''
	def component_function(self):

		'''Print the name of the composite object'''
		print("{}".format(self.name))

		'''Iterate through the child objects and invoke their component function and print their names'''
		for i in self.children:
			i.component_function()



#Build a composite submenu1. It is not a top level menu, but it is a composite in itself and has its own children

sub1 = Composite("Rices")

#Build a child sub-submenu11
sub11 = Child("Curd Rice")
sub12 = Child("Biriyani")

sub1.append_child(sub11)
sub1.append_child(sub12)

#Build a top-level composite menu
top = Composite("Indian cuisines")

#Build a simple submenu2 which is not a composite menu
sub2 = Composite("Breads")

#Add composite submenu to the top menu
top.append_child(sub1)
top.append_child(sub2)

#Test the composite pattern

top.component_function()