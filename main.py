#Introduces the joke game
import time
score = 0
print ("Welcome to the joke game")
time.sleep(3)
print ("Here is the 1st Joke!")
#\n shows a New Line
print("\n")
time.sleep(2)
print ("What is pink and fluffy")
a = str(input())
if a == str("Pink Fluff"):
  print ("You are Correct")
  score = score + 1
print ("\n")