import random as rd
import math
print('Guess number between 1 and 1000. You can enter 0 to quit!!!\n')
answer=rd.randint(1,1001)
max_guess = math.floor(math.log2(1000))
no_of_guess = 0
while True:
    try:
        no_of_guess += 1
        if no_of_guess > max_guess:
            print(f'You have exceeded your guess limit!!! Correct answer is {answer}. Thanks for playing')
            break
        guess=int(input('Enter your guess:'))
        if guess == 0:
            print('Thank for playing!!')
            break
        if 0<int(guess)<1001:
            if guess==answer:
                print("Great job..... You Won!!!!!")
                break
            elif guess < answer:
                print("Number is higher!!!!!")
            else:
                print('Number is lower!!!!!')
        else:
            print('Please enter between 1-10')
    except ValueError:
        print('Please enter integer only')
