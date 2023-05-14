row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]

def X(inp):
    if inp == "TL" and row1[0] == "":
        row1[0] = 'x'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "TM" and row1[1] == "":
        row1[1] = 'x'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "TR" and row1[2] == "":
        row1[2] = 'x'
        print(row1)
        print(row2)
        print(row3)

    elif inp == "ML" and row2[0] == "":
        row2[0] = 'x'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "MM" and row2[1] == "":
        row2[1] = 'x'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "MR" and row2[2] == "":
        row2[2] = 'x'
        print(row1)
        print(row2)
        print(row3)

    elif inp == "BL" and row3[0] == "":
        row3[0] = 'x'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "BM" and row3[1] == "":
        row3[1] = 'x'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "BR" and row3[2] == "":
        row3[2] = 'x'
        print(row1)
        print(row2)
        print(row3)

def O(inp):
    if inp == "TL" and row1[0] == "":
        row1[0] = 'o'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "TM" and row1[1] == "":
        row1[1] = 'o'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "TR" and row1[2] == "":
        row1[2] = 'o'
        print(row1)
        print(row2)
        print(row3)

    elif inp == "ML" and row2[0] == "":
        row2[0] = 'o'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "MM" and row2[1] == "":
        row2[1] = 'o'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "MR" and row2[2] == "":
        row2[2] = 'o'
        print(row1)
        print(row2)
        print(row3)

    elif inp == "BL" and row3[0] == "":
        row3[0] = 'o'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "BM" and row3[1] == "":
        row3[1] = 'o'
        print(row1)
        print(row2)
        print(row3)
    elif inp == "BR" and row3[2] == "":
        row3[2] = 'o'
        print(row1)
        print(row2)
        print(row3)

def check_winner():
    # Check rows
    for row in [row1, row2, row3]:
        if row[0] == row[1] == row[2] != "":
            return row[0]      

    # Check columns
    for col in range(3):
        if row1[col] == row2[col] == row3[col] != "":
            return row1[col]

    # Check diagonals
    if row1[0] == row2[1] == row3[2] != "":
        return row1[0]
    if row1[2] == row2[1] == row3[0] != "":
        return row1[2]

    return None

def check_draw():
    for row in [row1, row2, row3]:
        if "" in row:
            return False
    return True

while True:
    inp = input("where do you want to play? (X) ")
    X(inp)
    winner = check_winner()
    if winner:
        print(f"Player {winner} wins!")
        break
    elif check_draw():
        print("Draw!")
        break

    inp = input("where do you want to play? (O) ")
    O(inp)
    winner = check_winner()

    if winner:
        print(f"Player {winner} wins!")
        break
    elif check_draw():
        print("Draw!") 
        break