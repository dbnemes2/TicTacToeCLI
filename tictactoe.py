
board = [["*" for _ in range(3)] for _ in range(3)]
player = 0
p_symb = {0: "X", 1:"O"}

def main():
    global player
    print("Starting tic-tac-toe...enter 'end' or 'exit' to stop")

    while True:
        print_board()
        choice = input(f"Enter move for player {p_symb[player]}: ")

        match choice:
            case "end":
                return
            case "exit":
                return
            case _:
                if not choice.isdigit():
                    print("Invalid choice, choose 1-9")
                num = int(choice)
                if num < 0 or num > 9:
                    print("Invalid choice, choose 1-9")
                play(num)
                if check_for_winner():
                    again = input("Do you want to play again? (Y/N)").strip()
                    if again.lower() == "y":
                        for i in range(3):
                            for j in range(3):
                                board[i][j] = "*"
                        continue
                    else:
                        #for simplicity taking all non "Y" as "N"
                        return

                #now switch player
                player ^= 1



def play(position):
    #position in numpad notation 1-9
    # 7 8 9
    # 4 5 6
    # 1 2 3

    r, c = numpad_to_2d(position)
    board[r][c] = p_symb[player]

def check_for_winner():
    #using magic numbers because tic-tac_toe is always 3x3
    #checking rows and cols first
    for i in range(3):
        if board[i][0] != "*" and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            print(f"Player {board[i][0]} wins!")
            return True
        if board[0][i] != "*" and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            print(f"Player {board[0][i]} wins!")
            return True
    #now check diagonals
    if board[1][1] == "*":
        return False
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        print(f"Player {board[1][1]} wins!")
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        print(f"Player {board[1][1]} wins!")
        return True

    return False

def numpad_to_2d(id):
    row = 2 - ((id-1) // 3)
    col = (id-1) % 3
    return row, col

def print_board():
    for row in board:
        print(f"{row[0]} {row[1]} {row[2]}")


if __name__ == "__main__":
    main()

