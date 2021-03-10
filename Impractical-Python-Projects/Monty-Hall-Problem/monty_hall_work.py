Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import randint
>>> trials = 100000
>>> success = 0
>>> for trial in range(trials):
	faces = set()
	for rolls in range(6):
		roll = randint(1, 6)
		faces.add(roll)
		if len(faces) == 6:
			success += 1

			
>>> 
>>> print("probability of success = {}".format(success/trials))
probability of success = 0.01581
>>> 
 RESTART: C:/Users/qwert/Desktop/Scripts/Impractical-Python-Projects/Monty-Hall-Problem/monty_hall_mcs.py 
Input number of runs [20000]: 
Wins with original pick = 0
Wins with changed pick = 1
Probability of winning with initial guess: 0.00
Probability of winning by switching: 0.00

Press Enter key to exit.
>>> 
 RESTART: C:/Users/qwert/Desktop/Scripts/Impractical-Python-Projects/Monty-Hall-Problem/monty_hall_mcs.py 
Input number of runs [20000]: 
Wins with original pick = 6704
Wins with changed pick = 13296
Probability of winning with initial guess: 0.34
Probability of winning by switching: 0.66

Press Enter key to exit.
>>> 
 RESTART: C:/Users/qwert/Desktop/Scripts/Impractical-Python-Projects/Monty-Hall-Problem/monty_hall_mcs.py 
Input number of runs [20000]: 100000
Wins with original pick = 33253
Wins with changed pick = 66747
Probability of winning with initial guess: 0.33
Probability of winning by switching: 0.67

Press Enter key to exit.
>>> import random
>>> Class Dwarf(object):
	
SyntaxError: invalid syntax
>>> import random
>>> class Dwarf():
	def __init__(self, name):
		self.name = name
		self.attack = 3
		self.defend = 4
		self.body = 5
	def talk(self):
		print("I'm a blade-man, I'll cut ya!!!")

		
>>> lenn = Dwarf("Lenn")
>>> print("Dwarf name = {}".format(lenn.attack))
Dwarf name = 3
>>> print("Dwarf name = {}".format(lenn.name))
Dwarf name = Lenn
>>> print("Lenn's attack strength = {}".format(lenn.attack))
Lenn's attack strength = 3
>>> lenn.talk()
I'm a blade-man, I'll cut ya!!!
>>> class Elf():
	def __init__(self, name):
		self.name = name
		self.attack = 4
		self.defend = 4
		self.body = 4

		
>>> esseden = Elf("Esseden")
>>> print("Elf name = {}".format(esseden.name))
Elf name = Esseden
>>> print("Esseden body value = {}".format(esseden.body))
Esseden body value = 4
>>> 
>>> lenn_attack_roll = random.randrange(1, lenn.attack + 1)
>>> print(""Lenn_attack _roll = )
SyntaxError: invalid syntax
>>> print("Len attack roll = {}".format(lenn_attack_roll))
Len attack roll = 3
>>> esseden_defend_roll = random.randrange(1, esseden.defend + 1)
>>> print("Esseden defend roll = {}".format(esseden_defend_roll))
Esseden defend roll = 2
>>> 
>>> damage = lenn_attack_roll - esseden_defend_roll
>>> if damage > 0:
	esseden.body -= damage

	
>>> print("Esseden body value {}")
Esseden body value {}
>>> print("Esseden body value = {}".format(esseden.body))
Esseden body value = 3
>>> 
 RESTART: C:/Users/qwert/Desktop/Scripts/Impractical-Python-Projects/Monty-Hall-Problem/monty_hall_gui.py 
>>> 
