import tkinter as tk
from tkinter import messagebox

class UltimateTicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Ultimate Tic-Tac-Toe")
        self.current_player = 'X'
        self.big_board = [['' for _ in range(3)] for _ in range(3)]
        self.small_boards = [[[['' for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.active_board = None
        self.create_board()

    def create_board(self):
        self.buttons = [[[[None for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                frame = tk.Frame(self.master, borderwidth=3, relief="raised")
                frame.grid(row=i, column=j, padx=5, pady=5)
                for x in range(3):
                    for y in range(3):
                        self.buttons[i][j][x][y] = tk.Button(frame, text='', font=('normal', 20, 'bold'), width=3, height=1,
                                                             command=lambda r=i, c=j, x=x, y=y: self.on_click(r, c, x, y))
                        self.buttons[i][j][x][y].grid(row=x, column=y)

    def on_click(self, big_row, big_col, small_row, small_col):
        if self.active_board is not None and (big_row, big_col) != self.active_board:
            return
        if self.small_boards[big_row][big_col][small_row][small_col] or self.big_board[big_row][big_col]:
            return

        self.small_boards[big_row][big_col][small_row][small_col] = self.current_player
        self.buttons[big_row][big_col][small_row][small_col].config(text=self.current_player)

        if self.check_small_winner(big_row, big_col):
            self.big_board[big_row][big_col] = self.current_player
            for x in range(3):
                for y in range(3):
                    self.buttons[big_row][big_col][x][y].config(bg='red' if self.current_player == 'X' else 'green')

        if self.check_big_winner():
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins the game!")
            self.master.quit()
        elif all(all(cell for cell in row) for row in self.big_board):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.master.quit()

        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.active_board = (small_row, small_col) if not self.big_board[small_row][small_col] else None

        if self.active_board is None:
            for i in range(3):
                for j in range(3):
                    if not self.big_board[i][j]:
                        for x in range(3):
                            for y in range(3):
                                self.buttons[i][j][x][y].config(bg='SystemButtonFace')
        else:
            for i in range(3):
                for j in range(3):
                    for x in range(3):
                        for y in range(3):
                            if (i, j) == self.active_board:
                                self.buttons[i][j][x][y].config(bg='yellow')
                            elif not self.big_board[i][j]:
                                self.buttons[i][j][x][y].config(bg='SystemButtonFace')

    def check_small_winner(self, big_row, big_col):
        board = self.small_boards[big_row][big_col]
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '':
                return True
            if board[0][i] == board[1][i] == board[2][i] != '':
                return True
        if board[0][0] == board[1][1] == board[2][2] != '':
            return True
        if board[0][2] == board[1][1] == board[2][0] != '':
            return True
        return False

    def check_big_winner(self):
        for i in range(3):
            if self.big_board[i][0] == self.big_board[i][1] == self.big_board[i][2] != '':
                return True
            if self.big_board[0][i] == self.big_board[1][i] == self.big_board[2][i] != '':
                return True
        if self.big_board[0][0] == self.big_board[1][1] == self.big_board[2][2] != '':
            return True
        if self.big_board[0][2] == self.big_board[1][1] == self.big_board[2][0] != '':
            return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = UltimateTicTacToe(root)
    root.mainloop()
