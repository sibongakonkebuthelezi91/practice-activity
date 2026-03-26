import random


def get_last_life():

    last_life = ["This is my final chance…",
                    "Last life. No pressure 😬",
                    "All or nothing now!",
                    "Final guess coming up...",
                    "I can`t mess this up!",
                    "One shot left!",
                    "Do or die!",
                    "This is it… my last try!",
                    "No more mistakes allowed!",
                    "Everything depends on this guess!",
                    "I`m down to my last life 😭",
                    "Final attempt… let`s go!",
                    "Make it count!",
                    "This better be right!",
                    "My last hope 🤞"]
    return random.choice(last_life)


def win():
    win = ["Too easy 😎",
           "I told you I`d win.",
           "Light work 🥱",
           "Was that even a challenge?",
           "I don`t miss.",
           "Expected nothing less from me.",
           "Built different 💪",
           "That`s just how I operate.",
           "Another day, another win.",
           "I make this look easy.",
           "Stay mad 😌",
           "Outplayed. Completely.",
           "You really thought you had me?",
           "I`m him. 🐐",
           "Practice makes perfect… and I`m already perfect.",
           "Never in doubt.",
           "Levels to this.",
           "I run this.",
           "Don`t worry, I`ll go easy next time 😉",
           "That`s game."]
    return random.choice(win)


def must_be_number(num):
    global frustrate
    frustrate = ["Oh wow… didn`t see that coming (again)."
                 "Take your time… I`ll just wait forever.",
                 "Interesting choice…",
                 "Sure, let`s keep doing the same thing.",
                 "At this point, I`m not even surprised."]
    if num.isdigit():
        return int(num)
    else:
        while not num.isdigit():
            print(random.choice(frustrate))
            num = input("Enter numerical character ")
    return int(num)


def list_of_numbers(stop: int, start: int = 1):
    numbers = list(range(start, stop + 1))
    if len(numbers) >= 2:
        return numbers, 2
    else:
        while not numbers:
            print("Your stop should be bigger than your start")
            print(random.choice(frustrate).upper())
            start = must_be_number(input("Which number do you want to start at ? "))
            stop = must_be_number(input("What is your stop number: "))
            numbers = list(range(start, stop + 1))
        if len(numbers) < 2:
            return numbers, 0


def yes_no(confirm):
    if confirm.lower() == "y" or confirm.lower() == "n":
        return confirm
    else:
        confirm = ""
        while not confirm:
            confirm = input("Invalid selection: ")
            if confirm.lower() == "y" or confirm.lower() == "n":
                break
    return confirm