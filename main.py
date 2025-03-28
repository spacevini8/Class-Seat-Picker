import random

print("#################################################")
print("Welcome to class seating picker extravaganza!")
print("v0.1α")
print("In loving memory of my sanity")
print("Developed by spacevini8")
print("#################################################")
print("")
print("classes:")
print("1. History")
print("2. Maths")
print("q. exit")

Class = input("Enter the class number: ")

while True:
    if Class == "1":
        seat_number = random.sample(range(1, 30), 29)
        print("|", (seat_number[0]), "|", (seat_number[1]), "|", (seat_number[2]), "|", "", "", "", "", "", "", "", "", "|", (seat_number[3]), "|", (seat_number[4]), "|") # row 1
        print("|", (seat_number[5]), "|", (seat_number[6]), "|", (seat_number[7]), "|", (seat_number[8]), "|", "", "", "|", (seat_number[9]), "|", (seat_number[10]), "|", (seat_number[11]), "|", (seat_number[12]), "|") # row 2
        print("|", (seat_number[13]), "|", (seat_number[14]), "|", (seat_number[15]), "|", (seat_number[16]), "|", "", "", "|", (seat_number[17]), "|", (seat_number[18]), "|", (seat_number[19]), "|", (seat_number[20]), "|") # row 3
        print("|", (seat_number[21]), "|", (seat_number[22]), "|", (seat_number[23]), "|", (seat_number[24]), "|", "", "", "|", (seat_number[25]), "|", (seat_number[26]), "|", (seat_number[27]), "|", (seat_number[28]), "|") # row 4
        print("")
        repeat = input("Do you want to pick again? ((default) Y/n): ")
        if repeat == "y" or repeat == "Y" or repeat == "":
            continue
        elif repeat == "n" or repeat == "N":
            break
        else:
            break
    elif Class == "2":
        seat_number = random.sample(range(1, 30), 29)
        print("|", (seat_number[0]), "|", (seat_number[1]), "|", (seat_number[2]), "|", "", "", "", "", "|", (seat_number[3]), "|", (seat_number[4]), "|", (seat_number[5]), "|", "", "", "", "", "|", (seat_number[6]), "|", (seat_number[7]), "|", (seat_number[8]), "|") # row 1
        print("|", (seat_number[9]), "|", (seat_number[10]), "|", (seat_number[11]), "|", (seat_number[12]), "|", "", "", "|", (seat_number[13]), "|", (seat_number[14]), "|", (seat_number[15]), "|", "", "", "|", (seat_number[16]), "|", (seat_number[17]), "|", (seat_number[18]), "|") # row 2
        print("|", (seat_number[19]), "|", (seat_number[20]), "|", (seat_number[21]), "|", (seat_number[22]), "|", "", "", "|", (seat_number[23]), "|", (seat_number[24]), "|", (seat_number[25]), "|", "", "", "|", (seat_number[26]), "|", (seat_number[27]), "|", (seat_number[28]), "|") # row 3
        print("")
        repeat = input("Do you want to pick again? ((default) Y/n): ")
        if repeat == "y" or repeat == "Y" or repeat == "":
            continue
        elif repeat == "n" or repeat == "N":
            break
        else:
            break
    elif Class == "debug" or Class == "d":
        seat_number = random.sample(range(1, 30), 29)

        print(seat_number[0])  # Access the first element
        print(seat_number)     # Print the entire list
        exit()
    elif Class == "exit" or Class == "quit" or Class == "q":
        exit()
    else:
        print("Invalid class number")
        exit()