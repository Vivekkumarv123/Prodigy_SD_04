import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.board = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.master, width=3, font=('Arial', 14), textvariable=self.board[i][j], justify='center')
                entry.grid(row=i, column=j)
        
        solve_button = tk.Button(self.master, text="Solve", command=self.solve)
        solve_button.grid(row=9, columnspan=9)

    def solve(self):
        board = self.get_board()
        if self.solve_sudoku(board):
            self.update_grid(board)
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists for the given Sudoku puzzle.")

    def solve_sudoku(self, board):
        empty = self.find_empty_location(board)
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid_location(board, row, col, num):
                board[row][col] = num
                if self.solve_sudoku(board):
                    return True
                board[row][col] = 0

        return False

    def find_empty_location(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def is_valid_location(self, board, row, col, num):
        return (
            not any(num == board[row][i] for i in range(9)) and
            not any(num == board[i][col] for i in range(9)) and
            not any(num == board[row // 3 * 3 + i][col // 3 * 3 + j] for i in range(3) for j in range(3))
        )

    def get_board(self):
        board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                try:
                    val = int(self.board[i][j].get())
                    if 1 <= val <= 9:
                        board[i][j] = val
                    else:
                        board[i][j] = 0
                        self.board[i][j].set('')
                except ValueError:
                    self.board[i][j].set('')
        return board

    def update_grid(self, board):
        for i in range(9):
            for j in range(9):
                self.board[i][j].set(board[i][j])

def main():
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

'''example sudoko
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]'''