



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
        if self.is_empty([row][col]):
            self.board[row][col] = marker
            return True
        else:
            return False

    def is_full(self):
        counter = 0
        for n,lista in enumerate(self.board):
            for k,val in enumerate(lista):
                if not self.is_empty[n][k]:
                    counter += 1
        
        if counter == 9:
            return True
        else: 
            return False
                


    def is_winner(self,marker):
   
        #Rows
        for row in self.board:
            if len(set(row)) == 1:
                return True
        #Columns
        
        for row in self.board:
            if self.board[row][0] != marker:
                return False
            elif self.board[row][1] != marker:
                return False
            elif self.board[row][2] != marker:
                return False
        return True
                
            
            
            

    def restart(self):
        self.board = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']]

    def print_board(self):
        print(f"board: {self.board}")

board = TicTacToeBoard()
print(board.is_empty(1,1))