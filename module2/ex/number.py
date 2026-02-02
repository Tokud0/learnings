import random

def guess_number():
    
    secret = random.randint(1, 100)
    tries = 0

    while True:
        guess = int(input("Угадай число 1-100: "))
        tries += 1

        if guess < secret:
            print("Мало")
        elif guess > secret:
            print("Много")
        else:
            print(f"Верно. Попыток: {tries}")
            break

guess_number()