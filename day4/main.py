from pathlib import Path

def read_input(file_name: str) -> str:
    return (Path(__file__).parent / file_name).read_text()

def search_by_letter(data:str):
    crossword = data.split()
    # cardinals
    leftR = 0
    rightL = 0
    upD = 0
    downU = 0

    # diagonals
    leftRD = 0
    leftRU = 0
    rightLD = 0
    rightLU = 0

    for y, word in enumerate(crossword):
        for x, chara in enumerate(word):
            if(chara == 'X'):
                #Cardinals
                # left to right
                try:
                    if(f'{word[x]}{word[x+1]}{word[x+2]}{word[x+3]}' == 'XMAS'):
                        leftR += 1
                except IndexError:
                    pass

                # right to left
                try:
                    if(f'{word[x]}{word[x-1]}{word[x-2]}{word[x-3]}' == 'XMAS' and x-3>=0):
                        rightL += 1
                except IndexError:
                    pass

                # up to down
                try:
                    if(f'{word[x]}{crossword[y+1][x]}{crossword[y+2][x]}{crossword[y+3][x]}' == 'XMAS'):
                        upD += 1
                except IndexError:
                    pass

                # down to up
                try:
                    if(f'{word[x]}{crossword[y-1][x]}{crossword[y-2][x]}{crossword[y-3][x]}' == 'XMAS' and y-3>=0):
                        downU += 1
                except IndexError:
                    pass

                # Diagonals
                # left to right down
                try:
                    if(f'{word[x]}{crossword[y+1][x+1]}{crossword[y+2][x+2]}{crossword[y+3][x+3]}' == 'XMAS'):
                        leftRD += 1
                except IndexError:
                    pass

                # left to right up
                try:
                    if(f'{word[x]}{crossword[y-1][x+1]}{crossword[y-2][x+2]}{crossword[y-3][x+3]}' == 'XMAS' and y-3>=0):
                        leftRU += 1
                except IndexError:
                    pass

                # right to left down
                try:
                    if(f'{word[x]}{crossword[y+1][x-1]}{crossword[y+2][x-2]}{crossword[y+3][x-3]}' == 'XMAS' and x-3>=0):
                        rightLD += 1
                except IndexError:
                    pass

                # right to left up
                try:
                    if(f'{word[x]}{crossword[y-1][x-1]}{crossword[y-2][x-2]}{crossword[y-3][x-3]}' == 'XMAS' and x-3>=0 and y-3>=0):
                        rightLU += 1
                except IndexError:
                    pass

    # print(data)
    print(f'leftR: {leftR} rightL: {rightL} upD: {upD} downU: {downU}')
    print(f'leftR: {leftRD} rightL: {leftRU} upD: {rightLD} downU: {rightLU}')
    print(sum([leftR, rightL, upD, downU, leftRD, leftRU, rightLD, rightLU]))

def search_MAS(data:str):
    crossword = data.split()

    # diagonals
    leftRD = 0
    leftRU = 0
    rightLD = 0
    rightLU = 0

    for y, word in enumerate(crossword):
        for x, chara in enumerate(word):
            if(chara == 'A'):
                
                # Diagonals
                # left to right down
                try:
                    if((f'{crossword[y-1][x-1]}{crossword[y][x]}{crossword[y+1][x+1]}' == 'SAM' 
                        or f'{crossword[y-1][x-1]}{crossword[y][x]}{crossword[y+1][x+1]}' == 'MAS') 
                        and y-1 >= 0 and x-1 >= 0):

                        # left to right up

                        if((f'{crossword[y-1][x+1]}{word[x]}{crossword[y+1][x-1]}' == 'SAM' 
                            or f'{crossword[y-1][x+1]}{word[x]}{crossword[y+1][x-1]}' == 'MAS') 
                            and y-1 >= 0 and x-1 >= 0):
                            leftRU += 1
                        
                except IndexError:
                    pass


    # print(data)
    print(f'leftR: {leftRD} rightL: {leftRU} upD: {rightLD} downU: {rightLU}')
    print(sum([leftRD, leftRU, rightLD, rightLU]))


def main():
    data = read_input('data/inputData.txt')
    # search_by_letter(data)
    search_MAS(data)

if __name__ == "__main__":
    main()
