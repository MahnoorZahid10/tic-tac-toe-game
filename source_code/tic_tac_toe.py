import time
import datetime
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.WHITE + Back.RED)
print("           WELCOME                       " )
print("             TO                          " )
print("------TIC TAC TOE GAME-----              " )



''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []
#print(Fore.YELLOW+Back.RED)



for key in theBoard:
    board_keys.append(key)

def printDefaultBoard():
    print(Fore.YELLOW + Back.RED)
    print ("Kindly make your selection according to the board given below\n" )
    print('7' + '|' +'8' + '|' + '9')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('1' + '|' + '2' + '|' + '3\n\n')
    print(Fore.YELLOW + 'Lets Begin!' + Style.RESET_ALL)
    print(Style.RESET_ALL)
    

def printBoard(board):
    txt=''
    txt="\n"+board['7'] + '|' + board['8'] + '|' + board['9']+"\n-+-+-\n"+board['4'] + '|' + board['5'] + '|' + board['6']+"\n-+-+-\n"+ board['1'] + '|' + board['2'] + '|' + board['3'] +"\n"    
    print(txt)
    return txt
    
def game(player1,player2,mode):
    print(Fore.YELLOW + Back.RED)
    turn = 'X'
    count = 0
    player=player1
    proceed="True"

    while proceed:
     try:
      printBoard(theBoard)
      print("It's your turn," + player + ".Move to which place?")
      move = input()
      if(move!=''):
           if int(move) >0 and int(move)<=9:        
                if theBoard[move] == ' ':
                    theBoard[move] = turn
                    count += 1
                else:
                    print("That place is already filled.\nMove to which place?")
                    continue
                if count >= 5:
                    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                       txt=printBoard(theBoard)
                       printResult(player,txt,mode)
                       resetTheBoard(theBoard)  
                       proceed="False"             
                       return turn
                       
                    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                       txt=printBoard(theBoard)
                       printResult(player,txt,mode)
                       resetTheBoard(theBoard)
                       proceed="False"
                       return turn
                    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                       txt=printBoard(theBoard)
                       printResult(player,txt,mode)
                       resetTheBoard(theBoard)
                       proceed="False"
                       return turn
                    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                       txt=printBoard(theBoard)
                       printResult(player,txt,mode)
                       resetTheBoard(theBoard)
                       proceed="False"
                       return turn
                    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                       txt=printBoard(theBoard)
                       printResult(player,txt,mode)
                       resetTheBoard(theBoard)
                       proceed="False"
                       return turn
                    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                       txt=printBoard(theBoard)
                       printResult(player,txt,mode)
                       resetTheBoard(theBoard)
                       proceed="False"
                       return turn 
                    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                       txt=printBoard(theBoard)
                       printResult(player,txt,mode)
                       resetTheBoard(theBoard)
                       proceed="False"
                       return turn
                    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                       txt=printBoard(theBoard)
                       printResult(player,txt,mode)
                       resetTheBoard(theBoard)
                       proceed="False"
                       return turn 
                if count == 9:
                       txt=printBoard(theBoard)
                       printResult('',txt,mode)
                       resetTheBoard(theBoard)
                       proceed="False"
                       return ''
                      

        # Now we have to change the player after every move.
                if turn =='X':
                   turn = 'O'
                   player=player2
                else:
                   turn = 'X' 
                   player=player1 

           else:   
               print("Invalid selection,Kindly make selection according to the given board.")
               continue
      else:
         print("Input is empty,Kindly make selection according to the given board.")
         continue
     except:
         print("Input is invalid,Kindly enter numbers only.")
         continue
         
 
def writeResultInFile(text,mode):
    try:
     f = open("tictactoeGameResult.txt", "a") 
     s=str(datetime.datetime.now())
     f.write("-------TIC TAC TOE Game Result:"+s+"----------\n\n")
     if(mode==1):
      f.write("Noraml Mode :\n")
     elif(mode==2):
      f.write("Tournament Mode :\n")
     f.write(text)  
     f.close()
    except:
     print('Error Occured whie writing in a file.')
    else:
     print(Fore.WHITE+'Succefully written in a file'+Style.RESET_ALL)   

def date_time():
    return datetime.datetime.now()

def printResult(player,text,mode): 
    print("\nGame Over.\n")
    if(player==''):
       txt="It\'s a Tie!!\n" 
    else:
       txt=" **** " +player + " won. ****\n"
    print(txt)
    txt=txt+text
    writeResultInFile(txt,mode) 
                       

def resetTheBoard(board):
    for key in board_keys:
            theBoard[key] = " "

mode=0
user1=''
user2=''
while user1=='':
    user1=input("Please enter the name of player 1:" ) 
while user2=='':
    user2=input("Please enter the name of player 2:" )
while mode==0 or mode >2:
    try:
         mode=int(input("Please select mode: \n 1. Normal Mode \n 2. Tournament Mode\n" ) )
         if(mode>2):
             print("Kindly select 1 for normal mode and 2 for tournament mode.")
    except:
         print("Invalid Selection,Kindly select 1 for normal mode and 2 for tournament mode.")
if(mode==1):
  print("           WELCOME          ")
  print("             TO           " )
  print("---------Normal Mode------\n")
  print("Welcome "+user1+" as player1")
  print("Welcome "+user2+" as player2")
  printDefaultBoard()
  time.sleep(3)
  game(user1,user2,mode)


elif(mode==2):
 xCount=0
 oCount=0
 tCount=0
 print("           WELCOME          ")
 print("             TO           " )
 text="------Tournament Mode------"
 print (text)
 print ("In Tournament Mode the one who wins the most matches out of three is the winner------")
 print("Welcome "+user1+" as player1")
 print("Welcome "+user2+" as player2")
 tresult_col1=["\t|Game|","\t|"+user1+"|","\t|"+user2+"|"]
 tresult_col2=[]
 tournament_result_lst=[]
 tournament_result_lst.append(tresult_col1)
 for j in range(3):
        tCount=tCount+1
        print(Fore.BLUE+Back.RED+"-----------GAME "+str(j+1)+"---------------"+Style.RESET_ALL)
        tresult_col2.append("\t"+str(j+1))
        printDefaultBoard()
        game_rst=game(user1,user2,mode)
        if(game_rst=='X'):
            tresult_col2.append("\tWin")
            tresult_col2.append("\tLoss")
        elif(game_rst=='O'):
            tresult_col2.append("\tLoss")
            tresult_col2.append("\tWin")
        elif(game_rst==''):
            tresult_col2.append("\tTie")
            tresult_col2.append("\tTie") 
        tournament_result_lst.append(tresult_col2)
        tresult_col2=[]
        time.sleep(2)
 print(Fore.GREEN+"----Tournament Game Result------"+Style.RESET_ALL)       
 for k in tournament_result_lst:
    for p in k:
       print(p,end=' ')
    print()
 print(Style.RESET_ALL)
time.sleep(1000)


 
