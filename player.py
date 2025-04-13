class Player:

	def __init__(self, name):
		self.name = name
		self.hp = 100

	def damage(self, x):
		if (x == 1):
			self.hp-= 5
		elif(x == 2):
			self.hp-=7
		else:
			self.hp-=10

	def heal(self, y):
		self.hp+= (y*5)

	def disp(self):
		print('Name: ' + self.name)
		print('HP: ' + str(self.hp))



