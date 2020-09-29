#Introduces the joke game
import time
def jokes() :
  score = 0
  print ("Welcome to the joke game")
  time.sleep(3)
  print ("Here is the First Joke!")
  #\n shows a New Line
  print("\n")
  time.sleep(2)
  print ("What is pink and fluffy")
  a = str(input())
  if a == str("Pink Fluff"):
    print ("You are Correct")
    score = score + 1
    time.sleep(2)
    print(score)
  else :
    print ("You are wrong")
    time.sleep(2)
    score = score -1
    print(score)
    
if 1 == 1 jokes()




