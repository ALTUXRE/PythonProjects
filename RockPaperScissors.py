user1=input('Player1: ')
user2=input('Player2: ')
if user1=='Rock' and user2=='Scissors':
    print('user1 wins')
elif user1=='Rock' and user2=='Paper':
    print('user2 wins')
elif user1=='Rock' and user2=='Rock':
    print('tie')
if user2=='Rock' and user1=='Scissors':
    print('user2 wins')
elif user2=='Rock' and user1=='Paper':
    print('user1 wins')
elif user2=='Paper' and user1=='Paper':
    print('tie')
elif user1=='Scissors' and user2=='Scissors':
    print('tie')
#want to Play again
count=int(input('Want to play again ? (if yes enter 1 else enter 0)'))
if count==0:
    print('Game Over!')
    rate=int(input('Please rate the game out of 5 stars: '))
    print('Thank You for playing')
while count==1:
    user1=input('Player1: ')
    user2=input('Player2: ')
    if user1=='Rock' and user2=='Scissors':
        print('user1 wins')
    elif user1=='Rock' and user2=='Paper':
        print('user2 wins')
    elif user1=='Rock' and user2=='Rock':
        print('tie')
    if user2=='Rock' and user1=='Scissors':
        print('user2 wins')
    elif user2=='Rock' and user1=='Paper':
        print('user1 wins')
    elif user2=='Paper' and user1=='Paper':
        print('tie')
    elif user1=='Scissors' and user2=='Scissors':
        print('tie')
    count=int(input('Want to play again ? (if yes enter 1 else enter 0)'))
    if count==0:
        print('Game Over!')
        rate=int(input('Please rate the game out of 5 stars: '))
        print('Thank You for playing')
        break

