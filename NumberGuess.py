import random
options=(3,4,5,6,9,0,23,45)
actual_num=int(random.choice(options))
count=0
while True:
    count+=1
    num=int(input('Guess a Number: '))
    if num>actual_num:
     print('guess was too high')
    elif num<actual_num:
     print('guess was too low')
    if num == actual_num:
     print('You have guessed the number in ',count,' attempts')
     break
