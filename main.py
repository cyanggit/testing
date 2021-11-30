import random

while True:
      nummber1 = random.randrange(0,9)
      number2 = random.randrange(0,9)
      correctAnswer = number2 + nummber1

      answer = int(input("what is the sum of {} + {} = ?\n ".format(nummber1,number2)))

      if(correctAnswer != answer):
          print("False.That is incorrect.")
          break
      elif(correctAnswer == answer):
          print("True. That is correct".format(nummber1,number2,correctAnswer))
          break
