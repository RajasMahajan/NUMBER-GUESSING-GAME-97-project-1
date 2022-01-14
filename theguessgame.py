from random import randrange

num = randrange(1,9)
time = 0
number1 = int(90)
def wriththenub(number1): 
  
     number1 = int(input("guess number between 1 to 9: "))
     return number1
 
# ma'am i have added only 3 times its not because i don't know but because i like it
# you may increase times if you want :)
while time < 3:
     number1= wriththenub(number1)
     print(number1)
     if number1 == num:
           print("Congratulation YOU WON!!!")
           break 
     
     elif number1 < num:
               print('number is too less try other one')
               time=time+1
               
     elif number1 > num:
                          
          print('number is too big try other one')
          time=time+1

if not time < 3:
     print("You loss number is: ",num)
   
