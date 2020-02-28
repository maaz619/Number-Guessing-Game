import random as rd
print('For quitting type exit and hit enter!!!\n')
while True:
    try:
        answer=rd.randint(1,10)
        escape='exit'
        guess=(input('Enter your guess:'))
        if str(guess)==escape:
            print('Thank for playing!!')
            break
        if 0<int(guess)<11:
            if int(guess)==answer:
                print("Great job..... You Won!!!!!")
                break
            else:
                print('Keep tryin....')
        else:
            print('Please enter between 1-10')
    except ValueError:
        print('Please enter integer only')
