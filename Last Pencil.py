while True:
    a = input("How many pencils would you like to use:\n")
    if not a.isnumeric():
        print("The number of pencils should be numeric")
    elif int(a) <= 0:
        print("The number of pencils should be positive")
    else:
        a = int(a)
        break

while True:
    player_list = ["John", "Jack"]
    player = input("Who will be the first (John, Jack):\n")
    if player not in player_list:
        print(f"Choose between {player_list[0]} and {player_list[1]}")
    else:
        break


while a > 0:
    turn_list = ["1", "2", "3"]
    print(a * "|")
    print(f"{player}'s turn:\n")
    if player == "Jack":
        if a == 1:
            print("1")
            a = a -1
        elif a % 4 == 0:
            print("3")
            a = a - 3
        elif a % 4 == 3:
            print("2")
            a = a - 2
        elif a % 4 == 2:
            print("1")
            a = a - 1
        else:
            print("1")
            a = a - 1
    else:
        while True:
            turn = input()
            if turn not in turn_list:
                print("Possible values: '1', '2' or '3'")
            elif a - int(turn) < 0:
                print("Too many pencils were taken")
            else:
                a = a - int(turn)
                break
    if player == "John":
        player = "Jack"
    else:
        player = "John"

print(f"{player} won!")