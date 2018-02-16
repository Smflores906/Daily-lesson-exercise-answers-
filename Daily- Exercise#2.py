#Sebastian Flores - Daily Exercise - 02082018

#2. Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them 
#the year that they will turn 100 years old. Clue input()

Nombre = str(input(" Whats your name? "))

edad = str(input(" When were you born? "))

Future = int(edad) + 100
          
print ("You are " + Nombre + " and you were born in " + edad + " and you'll be 100 by the year " + str(Future))