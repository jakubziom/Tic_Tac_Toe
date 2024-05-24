# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:03:44 2024

@author: jakubziom
"""

import sys
sys.setrecursionlimit(15000)
import random

def Title():
    #prints title
    print(' ===============')
    print('   TIC-TAC-TOE')
    print(' ===============')
    print('type a1, b3, etc.')
    return

Title()

#defines size of the side of the board
while True:
    try:
        BoardSize=int(input('Board Size? 3-4?'))        
    except:
        continue    
    if  2 > BoardSize >5:
        continue
    elif 2 < BoardSize <5:
        break
         
#horizontal lines
Board0=[]
Board1=[]
Board2=[]
Board3=[]
Board4=[]
Board5=[]

'Player 1 = x'
'Player 2 = o'

#column letters transation to numbers
col={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}

BoardList=[Board0,Board1,Board2,Board3,Board4,Board5]

#number of marks in vertical lines (after player input)
Vx=[]
Vo=[]
#putting it together
V={'x':Vx,'o':Vo}

#number of marks in vertical lines (before player input)
OldVx=[]
OldVo=[]
#putting it together
OldV={'x':Vx,'o':Vo}

for i in range(0,BoardSize):
    #filling the lists to create the board
    for i in range(0,BoardSize):
        BoardList[i].insert(0,' ')
    #filling the lists to make vertical mark counters
    Vx.insert(0,0)
    Vo.insert(0,0)
    OldVx.insert(0,0)
    OldVo.insert(0,0)
    continue

def PrintBoard():
    #displays the board with separator lines (what player sees)
    BoardLetter=['    a','   b','   c','   d','   e','   f']
    #lists to put the horizontal line elements together
    LINE1=['1 │ ',]
    LINE2=['2 │ ',]
    LINE3=['3 │ ',]
    LINE4=['4 │ ',]
    LINE5=['5 │ ',]
    LINE6=['6 │ ',]

    BOARD=[LINE1,LINE2,LINE3,LINE4,LINE5,LINE6]

    for i in range(0,BoardSize):
        Letters=BoardLetter[slice(0,BoardSize)]
        lineSep='  ┼'+i*('───┼')+'───┼'
        for n in range(0,BoardSize):
                BOARD[n].append(BoardList[n][i])
                BOARD[n].append(' │ ')
    #lists for making final look of the horizontal lines
    line1=''
    line2=''
    line3=''
    line4=''
    line5=''
    line6=''
    letters=''
    lines=[line1,line2,line3,line4,line5,line6]
    for i in range(0,BoardSize):
        for a in BOARD[i]:
            #creates final looking lines with marks
            lines[i] += a
    for a in Letters:
        letters += a
    print(letters)
    print(lineSep)
    for i in range(0,BoardSize):
        print(lines[i])
        print(lineSep)
    return

def PrintCredits():
    #it prints credits after the game
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('Created by jakubziom 2024')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    
    return

PrintBoard()

def Player(mark):
    #putting the mark
    while True:
        #player input
        player=input(mark+'?') 
        try:
            r=(int(player[1:])-1)
        except:
            continue    
        c_input=player[0]
        if r >= BoardSize or r <=-1:
            continue
        #column translation from letter to number
        try:
            c=col[c_input]
        except:
            continue
        if c >= BoardSize or c <=-1:
            continue
        #condition to prevent from putting the mark again in same place
        if not (BoardList[r][c]=='x' or BoardList[r][c]=='o'):
                BoardList[r].pop(c)
                BoardList[r].insert(c, mark)
                PrintBoard()
                break       
        else:  
            continue  
    return  


def Congratulations(win,mark):
    #if one of the players wins
    win=True
    print(mark+' wins!')
    PrintCredits()
    input('press Enter to exit!')
    exit()
    return win,True

def PlayerWinsD1(mark,D1,win):
    #diagonal win 1
    for i in range(0,BoardSize):
        if BoardList[i][i]==mark:
            D1+=1   
    #this is for testing
    '''
    print('D1',mark,D1)
    '''
    if D1==BoardSize:
        Congratulations(win,mark)
        
        return True
    


def PlayerWinsD2(mark,D2,win):
    #diagonal win 2
    for i in range(0,BoardSize):
        if BoardList[BoardSize-1-i][i]==mark:
            D2+=1 
    #this is for testing
    '''
    print('D2',mark,D2)
    '''
    if D2==BoardSize:
        Congratulations(win,mark)
        return True

def OldMarkV(mark,OldV):
    #counting marks from previous round in vertical lines
    for i in range(0,BoardSize):
        for n in range(0,BoardSize):
            if BoardList[n][i]==mark:
                OldV[mark][i]+=1
    return OldV

def PlayerWinsV(mark,V):
    #vertical win
    for i in range(0,BoardSize):
        #substracting marks from previous round in vertical lines
        V[mark][i]-=(OldV[mark][i])
        #counting marks x or o in vertical lines
        for n in range(0,BoardSize):
            if BoardList[n][i]==mark:
                V[mark][i]+=1
                if V[mark][i]==BoardSize:
                    Congratulations(win,mark)
                    return True
    #this is for testing
    '''
    print('V',mark,V)
    '''
def PlayerWinsVC(mark,V):
    for i in range(0,BoardSize):
        V[mark][i]=0
    #vertical win
    for i in range(0,BoardSize):
        #substracting marks from previous round in vertical lines
        
        #counting marks x or o in vertical lines
        for n in range(0,BoardSize):
            if BoardList[n][i]==mark:
                V[mark][i]+=1
                #print(V[mark])
                if V[mark][i]==BoardSize:
                    return True

                    

#diagonal or horizontal win
def PlayerWinsDH(mark,win):
    #diagonal win
    PlayerWinsD1(mark,D1,win)
    PlayerWinsD2(mark, D2, win)
    for i in range(0,BoardSize):
        # horizontal win
        if BoardList[i].count(mark)==BoardSize:
            Congratulations(win,mark)
            return True
        


#values for checking draw
#is x in diagonal line 1?
D1Drawx=False
#is o in diagonal line 1?
D1Drawo=False
#is x in diagonal line 2?
D2Drawx=False
#is o in diagonal line 2?
D2Drawo=False
#putting it together
D1Draw={'x':D1Drawx,'o':D1Drawo}
D2Draw={'x':D2Drawx,'o':D2Drawo}

def Draw(win,mark):
    #diagonal draw 1
    for i in range(0,BoardSize):
        if BoardList[i][i]==mark:
            D1Draw[mark]=True   
    #this is for testing 
    '''
    print('D1Draw',D1Draw)
    '''
    #diagonal draw 2
    for i in range(0,BoardSize):
        if BoardList[BoardSize-1-i][i]==mark:
            D2Draw[mark]=True 
    #this is for testing
    '''
    print('D2Draw',D2Draw)
    '''
    VDrawCount=0
    HDrawCount=0
    #vertical draw
    for i in range(0,BoardSize):
        if V['x'][i]>=1 and V['o'][i]>=1:
            VDrawCount+=1
    #horizonal draw
    for i in range(0,BoardSize):
        if BoardList[i].count('x')>=1 and BoardList[i].count('o')>=1:
            HDrawCount+=1
    #this is for testing
    '''    
    print('VDrawCount',VDrawCount)
    print('HDrawCount',HDrawCount)
    '''
    #draw conditions
    if (D1Draw['x']==True and D1Draw['o']==True
        and D2Draw['x']==True and D2Draw['o']==True
        and VDrawCount==BoardSize
        and HDrawCount==BoardSize):      
        win=True
        print('DRAW!')
        PrintCredits()
        input('press Enter to exit!')
        exit()
        return win, True
    
def DrawC(win,mark):
    #diagonal draw 1
    for i in range(0,BoardSize):
        if BoardList[i][i]==mark:
            D1Draw[mark]=True   
    #this is for testing 
    '''
    print('D1Draw',D1Draw)
    '''
    #diagonal draw 2
    for i in range(0,BoardSize):
        if BoardList[BoardSize-1-i][i]==mark:
            D2Draw[mark]=True 
    #this is for testing
    '''
    print('D2Draw',D2Draw)
    '''
    VDrawCount=0
    HDrawCount=0
    #vertical draw
    for i in range(0,BoardSize):
        if V['x'][i]>=1 and V['o'][i]>=1:
            VDrawCount+=1
    #horizonal draw
    for i in range(0,BoardSize):
        if BoardList[i].count('x')>=1 and BoardList[i].count('o')>=1:
            HDrawCount+=1
    #this is for testing
    '''    
    print('VDrawCount',VDrawCount)
    print('HDrawCount',HDrawCount)
    '''
    #draw conditions
    if (D1Draw['x']==True and D1Draw['o']==True
        and D2Draw['x']==True and D2Draw['o']==True
        and VDrawCount==BoardSize
        and HDrawCount==BoardSize):      
        return win, True

def PlayerWinsD1C(mark,D1,win):
    D1=0
    #diagonal win 1
    for i in range(0,BoardSize):
        if BoardList[i][i]==mark:
            D1+=1  
    #print(D1)
    #this is for testing
    '''
    print('D1',mark,D1)
    '''
    if D1==BoardSize:       
        return True
    
def PlayerWinsD2C(mark,D2,win):
    D2=0
    #diagonal win 2
    for i in range(0,BoardSize):
        if BoardList[BoardSize-1-i][i]==mark:
            D2+=1 
    #print(D2)
    #this is for testing
    '''
    print('D2',mark,D2)
    '''
    if D2==BoardSize:
        return True    
    
def HorizontalWinC(mark):
    for i in range(0,BoardSize):
        #print(BoardList[i].count(mark))
        # horizontal win
        if BoardList[i].count(mark)==BoardSize:
            
            return True
    
def insertLetter(mark,n,i):
    if not (BoardList[n][i]=='x' or BoardList[n][i]=='o'):
        BoardList[n].pop(i)
        BoardList[n].insert(i, mark)
        PrintBoard()
    else:
        exit()
    return
    


def Computer(max_depth):
    
    max_score=-float('inf')
    best_moveR = 0
    best_moveC = 0
    
    for n in range(0,BoardSize):
        for i in range(0,BoardSize):
            if BoardList[n][i]==' ':
                BoardList[n].pop(i)
                BoardList[n].insert(i,'o')
                score = minimax(0,False,max_depth)
                BoardList[n].pop(i)
                BoardList[n].insert(i,' ')
                if score > max_score:
                    max_score = score
                    best_moveR = n
                    best_moveC= i
                    random_moveR = random.randint(0, BoardSize)
                    random_moveC= random.randint(0, BoardSize)

    
        #insertLetter('o', random_moveR,random_moveC)  
    
    insertLetter('o', best_moveR,best_moveC)
    return best_moveR,best_moveC
        


def minimax(depth, isMaximizing,max_depth):
    if HorizontalWinC('o') or PlayerWinsVC('o',V) or PlayerWinsD1C('o', D1, win) or PlayerWinsD2C('o',D2,win):
        return 1
    if HorizontalWinC('x') or PlayerWinsVC('x',V) or PlayerWinsD1C('x', D1, win) or PlayerWinsD2C('x',D2,win): 
        return -1
    
    if DrawC(win,'o') or DrawC(win,'x') or depth==max_depth:
        return 0
    
    
    if isMaximizing:
        max_score = -float('inf')
    
        for n in range(0,BoardSize):
            for i in range(0,BoardSize):
                if BoardList[n][i]==' ':
                    BoardList[n].pop(i)
                    BoardList[n].insert(i,'o')
                    score = minimax(depth+1,False,max_depth)
                    BoardList[n].pop(i)
                    BoardList[n].insert(i,' ')
                    
                    max_score = max(max_score, score)
        return max_score
    else:
        min_score = float('inf')
        for n in range(0,BoardSize):
            for i in range(0,BoardSize):
                if BoardList[n][i]==' ':
                    BoardList[n].pop(i)
                    BoardList[n].insert(i,'x')
                    score = minimax(depth+1,True,max_depth)
                    BoardList[n].pop(i)
                    BoardList[n].insert(i,' ')
                    
                    min_score = min(min_score, score)
        return min_score  

#number of horizontal and verical lines with x and o in them
HDrawCount=0
VDrawCount=0
#this just counts the loop
n=0
#number of x or o in diagonal line 1 and 2
D1=0
D2=0
#number of rounds (obsolete)
game=0
#if true the game ends (player wins or draw)
win=False
if BoardSize==3 :
    max_depth=5
elif BoardSize==4:
    max_depth=3
elif BoardSize==5:
    max_depth=3


while not win:
    #loop until the player wins or draw
    #x
    OldMarkV( 'x', OldV)
    Player('x')  
    PlayerWinsV('x',V)
    PlayerWinsDH('x',win)
    Draw(win,'x')
    game+=1
    #o
    OldMarkV( 'o', OldV)
    Computer(max_depth)  
    PlayerWinsV('o',V)
    PlayerWinsDH('o',win)
    Draw(win,'o')
    game+=1