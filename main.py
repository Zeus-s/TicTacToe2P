'''
func draws o and x
func for computer draws o
func check who win
'''

board = {'7' : ' ', '8' : ' ', '9' : ' ',
        '4' : ' ', '5' : ' ', '6' : ' ',
        '1' : ' ', '2' : ' ', '3' : ' ' }

bk = []

for key in board :
    bk.append(key)

def printboard(board) :
    print (board['7']+'|'+board['8']+'|'+board['9'])
    print ('-+-+-')
    print (board['4']+'|'+board['5']+'|'+board['6'])
    print ('-+-+-')
    print (board['1']+'|'+board['2']+'|'+board['3'])

def game() :
    cnt = 0
    draw = 'X'
    print("It's a TicTacToe Game made by Zeus-s for two players. Enjoy!\n")
    for i in range(10) :
        printboard(board)
        move = input("THE GAME : It's" + ' ' + draw + "'turn" + '. ' + "Input index which place do you want to fill? : ")
        if (board[move]==' ') :
            board[move] = draw
            cnt+=1
        else :
            print("THE GAME : This place has been filled, Please choose another place :")
            continue

        if (cnt>=5) :
            if (board['1']==board['2']==board['3']!=' ') :
                printboard(board)
                print("\nTHE GAME : Game's over!\n")
                print("\nTHE GAME : It's" + ' ' + draw + "'win!\n")
                break
            elif (board['4']==board['5']==board['6']!=' ') :
                printboard(board)
                print("\nTHE GAME : Game's over!\n")
                print("\nTHE GAME : It's" + ' ' + draw + "'win!\n")
                break
            elif (board['7']==board['8']==board['9']!=' ') :
                printboard(board)
                print("\nTHE GAME : Game's over!\n")
                print("\nTHE GAME : It's" + ' ' + draw + "'win!\n")
                break
            elif (board['7']==board['5']==board['3']!=' ') :
                printboard(board)
                print("\nTHE GAME : Game's over!")
                print("THE GAME : It's" + ' ' + draw + "'win!\n")
                break
            elif (board['1']==board['5']==board['9']!=' ') :
                printboard(board)
                print("\nTHE GAME : Game's over!\n")
                print("\nTHE GAME : It's" + ' ' + draw + "'win!\n")
                break
            elif (board['1']==board['4']==board['7']!=' ') :
                printboard(board)
                print("\nTHE GAME : Game's over!\n")
                print("\nTHE GAME : It's" + ' ' + draw + "'win!\n")
                break
            elif (board['3']==board['6']==board['9']!=' ') :
                printboard(board)
                print("\nTHE GAME : Game's over!\n")
                print("\nTHE GAME : It's" + ' ' + draw + "'win!\n")
                break
            elif (board['2']==board['5']==board['8'] !=' ') :
                printboard(board)
                print("\nTHE GAME : Game's over!\n")
                print("\nTHE GAME : It's" + ' ' + draw + "'win!\n")
                break
            
        if (cnt==9) :
            print("\nTHE GAME : Game's over!\n")
            print("THE GAME : It's a tie!")
            
        if draw == 'X' :
            draw = 'O'
        else :
            draw = 'X'

    restart = input("\nDo you want to play again? (y/n) :")
    if (restart.lower() =='y') :
        for key in bk :
            board[key] = " "
        game()
    else :
        print('\nGoodbye! Please close the application!')
    
if __name__ == "__main__":
    game()

        




