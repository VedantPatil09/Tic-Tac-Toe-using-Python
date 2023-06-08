def sum(a,b,c):
    return a + b + c

def printBoard(xState,zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print("---|---|---")
    print(f" {six} | {seven} | {eight} ")

def checkWin(xChance,yChance):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(xChance[win[0]],xChance[win[1]],xChance[win[2]]) == 3):
            print("X Won the Match")
            return 1
        if (sum(yChance[win[0]],yChance[win[1]],yChance[win[2]]) == 3):
            print("O Won the Match")
            return 0
    return -1


if __name__ == "__main__":
    xChance = [0,0,0,0,0,0,0,0,0]
    yChance = [0,0,0,0,0,0,0,0,0]
    # 1 for X and 0 for O
    turn = 1 
    print(" ********Welcome to Tic Tac Toe using Python******** ")
    while(True):
        try:
            printBoard(xChance,yChance)
            if(turn == 1):
                print("X's Chance")
                value = int(input("Please enter a value: "))
                xChance[value] = 1
            else:
                print("O's Chance")
                value = int(input("Please enter a value: "))
                yChance[value] = 1
            cwin = checkWin(xChance, yChance)
            if (cwin!= -1):
                print("Match Over")
                break

            turn = 1 - turn
        except IndexError:
            print("Entered value out of range!")
        except:
            print("Something went wrong! Game Over")
            break
            