row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]

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
