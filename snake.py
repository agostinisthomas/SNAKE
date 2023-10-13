import variables as vb

class Snake :
    def __init__(self, size) :
        self.size = size
        self.squares = []
        for i in range(size) :
            self.squares.append([vb.x0-i*10,vb.y0,1])

    def go_straight(self) :
        dir = self.squares[0][2]
        if dir == 1 :
            print("Going Right")
            self.squares = [[self.squares[0][0]+10,self.squares[0][1],1]] + self.squares
        elif dir == -1 :
            print("Going left")
            self.squares = [[self.squares[0][0]-10,self.squares[0][1],-1]] + self.squares
        elif dir == 2 :
            print("Going down")
            self.squares = [[self.squares[0][0],self.squares[0][1]+10,2]] + self.squares
        elif dir == -2 :
            print("Going up")
            self.squares = [[self.squares[0][0],self.squares[0][1]-10,-2]] + self.squares
        self.squares.pop()


    def change_direction(self,dir) :
        if dir == 1 :
            print("Going Right")
            self.squares = [[self.squares[0][0]+10,self.squares[0][1],dir]] + self.squares
        elif dir == -1 :
            print("Going left")
            self.squares = [[self.squares[0][0]-10,self.squares[0][1],dir]] + self.squares
        elif dir == 2 :
            print("Going down")
            self.squares = [[self.squares[0][0],self.squares[0][1]+10,dir]] + self.squares
        elif dir == -2 :
            print("Going up")
            self.squares = [[self.squares[0][0],self.squares[0][1]-10,dir]] + self.squares

        removed_square = self.squares.pop()

    def get_head_pos(self) :
        return [self.squares[0][0],self.squares[0][1]]

    def get_direction(self,square) :
        return self.squares[square][2]

    def grow(self) :
        if self.get_direction(-1) == 1 :
            self.squares.append([self.squares[-1][0]-10,self.squares[-1][1],self.squares[-1][2]])
        elif self.get_direction(-1) == -1 :
            self.squares.append([self.squares[-1][0]+10,self.squares[-1][1],self.squares[-1][2]])
        elif self.get_direction(-1) == 2 :
            self.squares.append([self.squares[-1][0],self.squares[-1][1]-10,self.squares[-1][2]])
        elif self.get_direction(-1) == -2 :
            self.squares.append([self.squares[-1][0],self.squares[-1][1]+10,self.squares[-1][2]])

    
