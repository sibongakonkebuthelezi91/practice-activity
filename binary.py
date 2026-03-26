from time import sleep
from random import shuffle
from action import (must_be_number,
                    win, get_last_life,
                    list_of_numbers,
                    yes_no)





def number_guessing_game(name):

    print(f"Hey {name} let me read your mind. 🔮")
    print("I give you a range of numbers and I will try to guess your number")
    start = must_be_number(input("Which number do you want to start at ? "))
    stop = must_be_number(input("What is your stop number: "))
    numbers, instruct = list_of_numbers(stop, start)
    shuffle(numbers)
    sleep(1.4)
    print("😤 YOU ARE NOT ALLOWED TO CHANGE A NUMBER!!! 😤")
    print("You have 10 seconds to choose a number.")
    sleep(1.30)
    print(f"Choose a number:\n{numbers}")
    sleep(10)
    print("Wait dont tell me!😏")
    sleep(2)
    print("I will try to guess your number I only have 7 tries.")
    sleep(1.30)
    print("But I will need clues from you.")
    sleep(1.20)
    print("tell me if I am high or low.")
    sleep(1.20)
    print("High means your number is bigger than mine.")
    sleep(1.20)
    print("Low means your number is lower than mine.")
    sleep(1.20)
    print("With that said let us start.😄")
    count = 0
    play = 1
    numbers = sorted(numbers)
    while True:
        computer_guess = 0
        # =============================
        # TWO NUMBERS LIST
        # =============================
        if not instruct:
            if len(numbers) == 1:
                print(f"This is your number {numbers[0]}")
                print(win())
                print("Do you want to go again!")
            hum_play = yes_no(input("(Y/n): "))
            if hum_play.lower() == "y":
                count = 0
                start = must_be_number(input("Which number do you want to start at  ? "))
                stop = must_be_number(input("What is your stop number: "))
                numbers, instruct = list_of_numbers(start, stop)
                shuffle(numbers)
                print(f"Choose a number:\n{numbers}")
                numbers = sorted(numbers)
                sleep(10)
                continue
            elif hum_play.lower() == "n":
                print("That was Fun see you next time.")
                break

        if play:
            if len(numbers) < 2:
                print(f"This is your number {numbers[0]}")
                hum_validate_ans = "y"
            else:
                computer_guess = (len(numbers)-1)//2
                print(f"Is this your number {numbers[computer_guess]}")
                hum_validate_ans = yes_no(input("Input (Y/n): "))
        if hum_validate_ans.lower() == "y":
            print(win())
            print("Do you want to go again!")
            hum_play = input("(Y/n): ")
            if hum_play.lower() == "y":
                count = 0
                start = must_be_number(input("Which number do you want to start at  ? "))
                stop = must_be_number(input("What is your stop number: "))
                numbers, instruct = list_of_numbers(stop, start)
                shuffle(numbers)
                print(f"Choose a number:\n{numbers}")
                numbers = sorted(numbers)
                sleep(10)
                continue
            elif hum_play.lower() == "n":
                print("That was Fun see you next time.")
                break
        elif hum_validate_ans.lower() == "n":
            play = 1
            count += 1
            print("Was it high or Low")
            hum_clue = input("High or Low: ")
            if count == 6:
                print(get_last_life())
            if numbers.index(numbers[computer_guess]) == 0:
                numbers = numbers[computer_guess + 1:]
            elif hum_clue.lower() == "high":
                numbers = numbers[computer_guess + 1:]
            elif hum_clue.lower() == "low":
                numbers = numbers[:computer_guess]
        else:
            play = 0


if __name__ == "__main__":
    number_guessing_game(input("What is your name: "))
