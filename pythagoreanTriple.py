#usr/bin/python

class TriangleChecker(object):
	
	def __init__(self, hyp, side1, side2):
		self.hyp = hyp
		self.side1 = side1
		self.side2 = side2
	
	def answer(self):
		hyp = self.hyp**2
		side1 = self.side1**2
		side2 = self.side2**2
		
		if hyp == side1 + side2:
			return "triangle is right angle"
		else:
			return "trianle is not right angle"



def main():
	
 
	print """
----------Find right angle triangles---------
this is how x, y, z react for the rest of program

     |\                                           
     | \                                         
     |  \                                        
    y|   \ x                                     
     |    \                                      
     |     \                                     
     |      \                                    
     ---------
	z

type your values for x ,y ,z (think of it as right angle for now)
"""


	x = input("x side: ")
	y = input("y side: ")
	z = input("z side: ")

	request = TriangleChecker(x, y, z)
	print request.answer()


if __name__ == '__main__':
	main()
