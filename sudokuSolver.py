#!/usr/bin/env python

class sudokuBoard():
    def __init__(self):
        self.board = [[-1 for x in range(9)] for y in range(9)]

    def printBoard(self):
        print "i  |j= 0   1   2   |   3   4   5   |   6   7   8  "
#             0  |   8   2   6   |   .   .   4   |   .   5   .
        print "   +----------------------------------------------",
        for x in range(9):
            if x % 3 ==0:
                print ""
            for y in range(9):
                if y == 0:
                    print "{}".format(x),
                if (y % 3) == 0:
                    print " | ",
                print " {} ".format(self.board[x][y] if self.board[x][y] != -1 else "."),
            print ""

    def insert(self,x,y,value):
        print "Inserting board[{}][{}] = {}".format(x,y,value)
        if self.board[x][y] != -1:
            print "Error: Space must be empty"
            return -1
        self.board[x][y]=value

    def getRow(self,x):
        return self.board[x]

    def getCol(self,y):
        return list(zip(*self.board)[y])

    def getSection(self,x,y):
        section = []
        for i in range(3):
            for j in range(3):
                section.append(self.board[int(x/3)*3+i][int(y/3)*3+j]) 
        return section

    def testValue(self,x,y,value):
        row = self.getRow(x)
        column = self.getCol(y)
        section = self.getSection(x,y)

        if value in row:
            print "{} found in row: {}".format(value,row)
            return -1;
        elif  value in column:
            print "{} found in column {}".format(value,column)
            return -1;
        elif value in section:
            print "{} found in section {}".format(value,section)
            return -1
        else:
            return 0;

class boardState():
    def __init__(self):
        self.boardState=[[range(1,10) for x in range(9)] for y in range(9)]

    def remove(self,x,y,value):
        print "Removing State: boardState[{}][{}]={}".format(x,y,value)
        self.boardState[x][y] = []
        for i in range(9):                
                sec_x =int(x/3)*3+ (i % 3)
                sec_y = int(y/3)*3 + int(i/3)

                #print "removing {} from ({},{})".format(value,x,i)
                try:
                    self.boardState[x][i].remove(value)
                except ValueError:
                    #print "can't remove {} from ({},{})={}".format(value,x,i,self.boardState[x][i])
                    pass

                #print "removing {} from ({},{})".format(value,i,y)
                try:
                    self.boardState[i][y].remove(value)
                except ValueError:
                    #print "Can't remove {} from ({},{})={}".format(value,i,y,self.boardState[i][y])
                    pass
                #print "removing {} from ({},{})".format(value,sec_x,sec_y)
                try:
                    self.boardState[sec_x][sec_y].remove(value)
                except ValueError:
                    #print "Can't remove {} from ({},{})={}".format(value,sec_x,sec_y,self.boardState[sec_x][sec_y])
                    pass
    def getMove(self):
        """ 
            return x,y position of next move, moves will be based on any cell that only has 1 move state
            there is going to be a better way to do this, but this will work for now
        """
        for i in range(9):
            for j in range(9):
                if len(self.boardState[i][j]) == 1:
                    return (i,j,self.boardState[i][j][0])
        return (-1,-1,0)

def main():
    print "Starting Sudoku solver!"
    board = sudokuBoard()
    state = boardState()
    init_board="8.6..4.5.5...1.8...13.5..47.9.64.........9...17...........38............738491.6."
    boardList=list(init_board)
    for i in range(9):
        for j in range(9):
            value = boardList[(i*9)+j]
            if value != '.':
                value = int(value)
                board.insert(i,j,value)
                state.remove(i,j,value)
    
    done  = False
    while not done:
        x,y,value = state.getMove()
        print x,y,value
        if x == -1 or y == -1:
            notDone = True;
            break;
        raw_input("Insert Board[{}][{}] =  {} ?...".format(x,y,value))
        board.insert(x,y,value)
        state.remove(x,y,value)

        board.printBoard()

    print "Done"
    board.printBoard()

if __name__ == "__main__":
    main()