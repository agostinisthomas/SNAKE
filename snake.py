import variables as vb

class Snake :
    def __init__(self, size) :
        self.size = size
        self.squares = []
        for i in range(size) :
            self.squares.append([vb.x0-i*15,vb.y0,1])

    def move(self) :
        print("In move function")
        if self.squares[0][2] == 1 :
            print("Going Right")
            self.squares = [[self.squares[0][0]+10,self.squares[0][1],1]] + self.squares
        elif self.squares[0][2] == -1 :
            print("Going left")
            self.squares = [[self.squares[0][0]-10,self.squares[0][1],1]] + self.squares
        elif self.squares[0][2] == 2 :
            print("Going down")
            self.squares = [[self.squares[0][0],self.squares[0][1]+10,1]] + self.squares
        elif self.squares[0][2] == -2 :
            print("Going up")
            self.squares = [[self.squares[0][0],self.squares[0][1]-10,1]] + self.squares

        removed_square = self.squares.pop()
        print("Move function removed : ",removed_square)    
            # if index>0 :
            #     sq[2] = self.squares[index]
        # On décale les carrés : le carré n prend la place du carré n-1 en partant de la tête
        # for sq_nb in range(len(self.squares)-1,0,-1) :
        #     print("Square Number : ",sq_nb)
        #     self.squares[sq_nb]=self.squares[sq_nb-1]


    def get_head_pos(self) :
        return [self.squares[0][0],self.squares[0][1]]

    def get_direction(self,square) :
        return self.squares[square][2]