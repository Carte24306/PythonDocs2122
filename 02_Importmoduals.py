#import the basics module to use its code
import basics
#make a new a application object from the basics module
app = basics.newProgram()
#use method that belongs to our new app;ication object
app.print("yo mama")
# print a property of our new application object
app.print( app.debugging )

#this line wont print if app.debugging is false
app.debug("Hello")

#we'll enable debgging for the application
app.debugging = True
app.debug("Now it works")

#import a defult python module
import random

#Use a method from the random module
randomNumber = random.randint(1, 10)
app.print(randomNumber)
