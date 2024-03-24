 #숫자 맞추기 게임

import random

random_number = random.randint(1,100)

count = 1

while True:
    try:
        number = int(input("1~100사이의 숫자 입력하세요"))

        if number > random_number:
            print("down")
        elif number < random_number:
            print("up")
        elif number == random_number:
            print("great! {}".format(count))
            break
        count = count +1

    except: 
        print("error. please enter the number")