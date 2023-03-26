



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
        else: 
            return False
        

    def place(self,marker, row, col):
        if self.is_empty(row,col):
            self.board[row][col] = marker
            return self.board
        else:
            return False

    def is_full(self):
        counter = 0
        for n,lista in enumerate(self.board):
            for k,val in enumerate(lista):
                if not self.is_empty(n,k):
                    counter += 1
        
        if counter == 9:
            return True
        else: 
            return False
                


    def is_winner(self,marker):
   
        #Rows
        for row in self.board:
     
            if marker in set(row) and len(set(row)) == 1:
                return True
        #Columns
        for col in range(3):
            checker = []
            for row in range(3):
                checker.append(self.board[row][col])
            if marker in set(checker) and len(set(checker)) == 1:
                return True
    
    
        #Diagonaler
        diagonal1 = [self.board[i][i] for i in range(len(self.board))]
        if marker in set(diagonal1) and len(set(diagonal1)) == 1:
            return True
            
        diagonal2 = [self.board[i][len(self.board)-1-i] for i in range(len(self.board))]
        if marker in set(diagonal2) and len(set(diagonal2)) == 1:
            return True
        
        return False
                

    def restart(self):
        self.board = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']]

    def print_board(self):
        print(f"board: {self.board}")




if __name__ == '__main__':

    b = TicTacToeBoard()
    b.place('O', 0, 0)
    b.place('O', 0, 1)
    b.place('O', 0, 2)
    print(b.board)
    print(b.is_winner('O'))
    print(b.restart())
    print(b.board)
