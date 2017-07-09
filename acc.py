class Account: #base Class object
    
	def __init__(self,filepath):
		self.filepath=filepath #instance variables
		with open(filepath, 'r') as file:
			self.balance=int(file.read())
    
	def withdraw(self, amount):
		self.balance = self.balance - amount
		
		
	def deposit(self, amount):
		self.balance = self.balance + amount
		
	def commit(self):
		with open(self.filepath,'w') as file:
			file.write(str(self.balance))
			
class Checking(Account): #Inheritance of the Account class
	""" This class generates checking account objects """ #Doc String

	type="checking" #data member also called a Class variable
	
	def __init__(self,filepath,fee): #constructor
		Account.__init__(self,filepath)
		self.fee=fee #data member
		
	def transfer(self,amount): #class method
		self.balance=self.balance-amount-self.fee

#jacks_checking is an Object instance		
jacks_checking=Checking("jack.txt",1) #instantiation of the class
jacks_checking.transfer(100)
jacks_checking.commit()
print(jacks_checking.balance)
print(jacks_checking.type)
            
johns_checking=Checking("john.txt",1)
johns_checking.transfer(100)
johns_checking.commit()
print(johns_checking.balance)
print(johns_checking.type) #method of accessing an attribute of the class

print(johns_checking.__doc__)