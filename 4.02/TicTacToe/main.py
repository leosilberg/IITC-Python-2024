import time
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.wins = 0
        self.loses = 0
        self.draws = 0

    def setPiece(self, piece: str):
        self.piece = piece

    def win(self):
        print(f"{self.name} has won")
        self.wins += 1

    def lose(self):
        self.loses += 1

    def draw(self):
        self.draws += 1
    
    def __str__(self) -> str:
        return f"\n{self.name}\nWins: {self.wins}\nLoses: {self.loses}\nDraws: {self.draws}\n"

def Analytics(func):
    def wrapper(self):
        start= time.perf_counter()
        func(self)
        end=time.perf_counter()
        return end - start
    return wrapper

class Game:
    def __init__(self, playerX: Player, playerO: Player) -> None:
        self.playerX = playerX
        self.playerO = playerO
        self.board = [str(i) for i in range(1, 10)]

    def displayBoard(self) -> str:
        print( f"\n{"|".join(self.board[0:3])}\n{"-----"}\n{"|".join(self.board[3:6])}\n{"-----"}\n{"|".join(self.board[6:9])}\n")
    
    def checkBoard(self):
        diag1=set(game.board[0::4])
        if len(diag1)==1:
            return diag1
        diag2=set(game.board[2:7:2])
        if len(diag2)==1:
            return diag2
        
        for i in range(3):
           row=set(self.board[3*i:3*(i+1)])
           if len(row)==1:
               return row
           col=set(self.board[i::3])
           if len(col)==1:
               return col
        return {i for i in self.board if i.isdigit()}
    
    def turn(self,player:Player):
        print(f"{player.name} your piece is {player.piece}")
        while True:
             pos=input(f"{player.name} pick a square\n")
             if pos not in [str(i) for i in range(1,10)]:
                 pos=input(f"Input must be digit between 1 and 9\n")
                 continue
             elif not self.board[int(pos)-1].isdigit():
                 print((f"The square {pos} is already marked with {self.board[int(pos)-1]}. Pick again\n"))
                 continue
             else:
                 self.board[int(pos)-1]=player.piece
                 break
        
    @Analytics      
    def start(self):
        self.displayBoard()
        result=self.checkBoard()
        while not result.issubset({"X","O"}) and len(result)!=0:
           self.turn(self.playerX if len(result)%2==1 else self.playerO)
           self.displayBoard()
           result=self.checkBoard()
    
        if self.playerX.piece in result:
            self.playerX.win()
            self.playerO.lose()
        elif self.playerO.piece in result:
            self.playerX.lose()
            self.playerO.win()
        else:
            self.playerX.draw()
            self.playerO.draw()
            print("Draw")

def addPlayer() -> Player:
    name = input(f"Please enter your name\n")
    return Player(name)


def choosePiece(name:str) -> str:
    pieces = ["X", "O"]
    while True:
        choice = input(f"{name} choose X or O\n")
        if choice.upper() in pieces:
            return choice.upper()


if __name__ == "__main__":

    print("1st player")
    player1 = addPlayer()
    print("2nd player")
    player2 = addPlayer()
    menu="y"
    while menu.lower()=="y":
        player1.setPiece(choosePiece(player1.name))
        player2.setPiece("O" if player1.piece == "X" else "X")
        game = Game(player1 if player1.piece=="X" else player2, player1 if player1.piece=="O" else player2)
        print(f"The game took {round(game.start())}s")
        print(game.playerX)
        print(game.playerO)
        menu=input(f"Would you like to play another game (Y) yes or (N) no\n")
    
    

