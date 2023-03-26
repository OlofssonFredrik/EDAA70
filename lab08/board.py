



class TicTacToeBoard:
    def __init__(self):
        self.board = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']]
                    
        
    def __str__(self):
        return f"{self.board}"
    
    def get(self,row, col):
        return self.board[row][col]

    def is_empty(self,row, col):
        if self.board[row][col] == '-':
            return True
        else: return False

    def place(self,marker, row, col):
        pass

    def is_full(self):
        pass


    def is_winner(self,marker):
        pass

    def restart(self):
        pass

    def print_board(self):
        pass

board = TicTacToeBoard()
print(board.is_empty(1,1))