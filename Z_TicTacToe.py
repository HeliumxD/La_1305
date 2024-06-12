import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def tic_tac_toe():
    def new_game():
        nonlocal board, current_player
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(text=" ", state=tk.NORMAL)

    def on_click(row, col):
        nonlocal current_player
        if board[row][col] == " ":
            board[row][col] = current_player
            buttons[row][col].config(text=current_player, state=tk.DISABLED)
            if check_win(board, current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
                disable_buttons()
            elif all(all(cell != " " for cell in row) for row in board):
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            else:
                current_player = "O" if current_player == "X" else "X"

    def disable_buttons():
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(state=tk.DISABLED)

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    root = tk.Tk()
    root.title("Tic Tac Toe")

    buttons = [[None for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(root, text=" ", font=('normal', 20), width=5, height=2,
                                          command=lambda row=row, col=col: on_click(row, col))
            buttons[row][col].grid(row=row, column=col)

    restart_button = tk.Button(root, text="New Game", command=new_game)
    restart_button.grid(row=3, column=0, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    tic_tac_toe()
