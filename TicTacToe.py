"""
Batool Raza
CS 100 2019S 
"""
import turtle
import random

def draw_board(t):
    t.pen(pensize = 5)
    screen = turtle.Screen()
    t.speed(15)
    t.hideturtle()
    t.pu()
    t.forward(100)
    t.left(90)
    t.forward(200)

    t.left(180)
    t.pd()
    t.forward(300)

    t.pu()
    t.right(90)
    t.forward(175)
    t.right(90)
    t.pd()
    t.forward(300)
    
    t.pu()

    t.setx(100)
    t.sety(15)
    t.left(90)
    t.bk(100)
    t.pd()
    t.forward(400)

    t.pu()
    t.setx(-100)
    t.sety(100)
    t.left(180)
    t.bk(100) 
    t.pd()
    t.forward(400)
def draw_O(x,y):
    z = turtle.Turtle()
    z.pen(pencolor = "FireBrick", pensize = 4)
    z.pu()
    z.speed(12)
    z.goto(x,y)
    z.pd()
    z.circle(20)
def draw_X(x,y):
    z = turtle.Turtle()
    z.pen(pencolor = "SlateGrey", pensize = 4)
    z.speed(5)
    z.pu()
    z.goto(x,y)
    z.left(45)
    z.pd()
    z.forward(50)
    z.pu()
    z.left(140)
    z.forward(35)
    z.left(140)
    z.pd()
    z.forward(50)

def isEmpty(board):
    
    countEmpty = 0
    for i in range(len(board)):
        if board[i] == " ":
            countEmpty += 1
    if countEmpty != 0:
        return True
    else:
        return False

def userInput(board):
   uturn = int(input("Enter a number, 1-9: "))
   if uturn <= 0 or uturn > 9:
        print("Number Must be Between 0 & 9")
        userInput(board)
   else:
       v = valid(uturn,board)
       if v == True:
           updateBoard(uturn, board, "x")
           mv = movePlayer(uturn,board,"x")
           if mv == True:
               mv =  True
           elif mv == "tie":
               mv = "tie"
           else:
               mv = False

           #print(mv)
           return mv
       else:
            print("Already Taken.")
            userInput(board)
    

def movePlayer(pos, board, s):
    draw(s, pos)
    checkwin = checkWin(board, s)
    checkTie = isEmpty(board)

    if checkwin == True:
        drawWinLine(board,s)
        return True
    elif checkTie == False:
        t = "tie"
        return t
    else:
        return False


def randomNum(board):
    n = False
    while n == False:
        num = random.randint(1,9)
        n = valid(num,board)
        if n == True:
            updateBoard(num, board, "o")
            mv = movePlayer(num, board, "o")
            if mv == True:
                mv = True
            elif mv == "tie":
               mv = "tie"
            else:
                return False
            return mv
    
def valid(num,board):    
    for c in board:
        if board[num] == " ":     
            return True
        else:
            return False

def draw(s, position):
    if s == "x":
        for i in range(1,9):
            if position == 1:
                draw_X(-145, 125)
                break
            elif position == 2:
                draw_X(0, 130)
                break
            elif position == 3:
                draw_X(145, 125)
                break
            elif position == 4:
                draw_X(-155, 55)
                break
            elif position == 5:
                draw_X(0, 40)
                break
            elif position == 6:
                draw_X(140, 45)
                break
            elif position == 7:
                draw_X(-155, -35)
                break
            elif position == 8:
                draw_X(0, -60)
                break
            elif position == 9:
                draw_X(140, -45)
                break
            else:
                break

    if s == "o":
        for i in range(1,9):
            if position == 1:
                draw_O(-145, 125)
                break
            elif position == 2:
                draw_O(0, 125)
                break
            elif position == 3:
                draw_O(145, 125)
                break
            elif position == 4:
                draw_O(-145, 35)
                break
            elif position == 5:
                draw_O(0, 40)
                break
            elif position == 6:
                draw_O(145, 35)
                break
            elif position == 7:
                draw_O(-145, -60)
                break
            elif position == 8:
                draw_O(0, -60)
                break
            elif position == 9:
                draw_O(145, -60)
                break
            else:
                break

   
def updateBoard(index,board,s):
    for i in range(len(board)):
        board[index] = s

def checkWin(board,s):
    if s == "x":
        if (board[1] == s and board[2] == s and board[3] == s ) or (board[4] == s and board[5] == s and board[6] == s) or (board[7] == s and board[8] == s and board[9] == s):
            return True            
        if (board[1] == s and board[4] == s and board[7] == s) or (board[2] == s and board[5] == s and board[8] == s) or (board[3] == s and board[6] == s and board[9] == s):
            return True
        if (board[1] == s and board[5] == s and board[9] == s) or (board[3] == s and board[5] == s and board[7] == s):
            return True

    if s == "o":
        if (board[1] == s and board[2] == s and board[3] == s ) or (board[4] == s and board[5] == s and board[6] == s) or (board[7] == s and board[8] == s and board[9] == s):
            return True 
        if (board[1] == s and board[4] == s and board[7] == s) or (board[2] == s and board[5] == s and board[8] == s) or (board[3] == s and board[6] == s and board[9] == s):
            return True
        if (board[1] == s and board[5] == s and board[9] == s) or (board[3] == s and board[5] == s and board[7] == s):
            return True


def drawWinLine(board, s):
    if s == "x":
        if (board[1] == s and board[2] == s and board[3] == s ):
            drawHorizontalLine(-145,145)
        elif (board[4] == s and board[5] == s and board[6] == s):
            drawHorizontalLine(-145,60)
        elif (board[7] == s and board[8] == s and board[9] == s):
            drawHorizontalLine(-145,-55)
        elif (board[1] == s and board[4] == s and board[7] == s):
            drawVerticalLine(-145,199)
        elif (board[2] == s and board[5] == s and board[8] == s):
             drawVerticalLine(3,199)
        elif (board[3] == s and board[6] == s and board[9] == s):
            drawVerticalLine(145,199)
        elif (board[1] == s and board[5] == s and board[9] == s):
            drawDiagonalLineL(-140,190)
        elif (board[3] == s and board[5] == s and board[7] == s):
            drawDiagonalLineR(145,160)

    if s == "o":
        if (board[1] == s and board[2] == s and board[3] == s ):
            drawHorizontalLine(-145,145)
        elif (board[4] == s and board[5] == s and board[6] == s):
            drawHorizontalLine(-145,60)
        elif (board[7] == s and board[8] == s and board[9] == s):
            drawHorizontalLine(-145,-55)
        elif (board[1] == s and board[4] == s and board[7] == s):
            drawVerticalLine(-145,199)
        elif (board[2] == s and board[5] == s and board[8] == s):
             drawVerticalLine(3,199)
        elif (board[3] == s and board[6] == s and board[9] == s):
            drawVerticalLine(145,199)
        elif (board[1] == s and board[5] == s and board[9] == s):
            drawDiagonalLineL(-140,190)
        elif (board[3] == s and board[5] == s and board[7] == s):
            drawDiagonalLineR(145,160)
            

        
def drawHorizontalLine(x,y):
    z = turtle.Turtle()
    z.pu()
    z.goto(x,y)
    z.pd()
    z.forward(350)
def drawVerticalLine(x,y):
    z = turtle.Turtle()
    z.pu()
    z.goto(x,y)
    z.right(90)
    z.pd()
    z.forward(300)
def drawDiagonalLineL(x,y):
    z = turtle.Turtle()
    z.pu()
    z.goto(x,y)
    z.right(35)
    z.pd()
    z.forward(399)
def drawDiagonalLineR(x,y):
    z = turtle.Turtle()
    z.pu()
    z.goto(x,y)
    z.right(155)
    z.pd()
    z.forward(399)

def firstTurn():
    turn = random.randint(0,1)
    num = int(input("Pick 0 or 1: "))
    while num < 0 or num > 1:
        print("Number must be between 0 or 1")
        num = int(input("Pick 0 or 1: "))
    else:
        if num == turn:
            return True
        else:
            return False
         
def playGameU(board,t):
    emp = isEmpty(board)
    while emp != False:
        gameOver = False

        while gameOver == False:
            gameOver = userInput(board)
            if gameOver == True:
                print("You Won!")
                reStart(t)
                break
            elif gameOver == "tie":
                gameOver = True
                print("It's a Tie!")
                reStart(t)
                break
            else:
                gameOver = randomNum(board)
                if gameOver == True:
                    print("AI Won!")
                    reStart(t)
                    break
        if gameOver == True:
            break
        else:
            continue
        emp = isEmpty(board)

def playGameAI(board,t):
    emp = isEmpty(board)
    while emp != False:
        gameOver = False

        while gameOver == False:
            gameOver = randomNum(board)
            if gameOver == True:
                print("AI Won!")
                reStart(t)
                break
            elif gameOver == "tie":
                gameOver = True
                print("It's a Tie!")
                reStart(t)
                break
            else:
                gameOver = userInput(board)
                if gameOver == True:
                    print("You Won!")
                    reStart(t)
                    break               
        if gameOver == True:
            break
        else:
            continue
        emp = isEmpty(board)

def startGame(board,t):
    ft = firstTurn()
    print(ft)
    if ft == True:
        print("You Go First")
        playGameU(board,t)
    else:
        print("AI Goes First")
        playGameAI(board,t)

def rePlay(t):
    board = ["freespace", " ", " ", " ", " ", " ", " ", " ", " "," "]
    for i in range(1, len(board)):
        if board[i] != " ":
            board[i] = " "

    turtle.resetscreen()
    draw_board(t)
    startGame(board,t)

def reStart(t):
    rp = input("Would you like to replay? Y or N: ")
    yes = rp.upper()
    if yes == "Y":
        rePlay(t)

print("\t\t\t ******Tic Tac Toe******")
t = turtle.Turtle()
board = ["freespace", " ", " ", " ", " ", " ", " ", " ", " "," "]
draw_board(t)
startGame(board,t)
