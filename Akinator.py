import random as rand
import time

print("Добрый день, сэр.")
time.sleep(1)
print("Я загадал число от 100 до 1.\nПопробуй отгадать!")

namber = rand.randint(1, 101)
guess = input()
guess = int(guess)
Guess_Of_namber = 0

while namber != guess:
    if guess > namber:
        print("Слишком много!")
        guess = input()
        guess = int(guess)
        Guess_Of_namber += 1

    if guess < namber:
        print("Слишком мало!")
        guess = input()
        guess = int(guess)
        Guess_Of_namber += 1

print("Ты угадал!\nЗа: ", Guess_Of_namber, end ='')
x = Guess_Of_namber + 1
if 11 <= x <= 19:
    print(" попыток")
else:
    if x % 10 == 1:
        print(" попытка")
    else:
        if 2 <= x % 10 <= 4:
            print(" попытки")
        else:
            print(" попыток")
