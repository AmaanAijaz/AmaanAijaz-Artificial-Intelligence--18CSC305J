def initialize(n): #initialize the board
  for key in ['queen','row','col','nwtose','swtone']:
    board[key] = {}
  for i in range(n):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][i] = 0
  for i in range(-(n-1),n):
    board['nwtose'][i] = 0
  for i in range(2*n-1):
    board['swtone'][i] = 0

def printboard(): #print the board
  for row in sorted(board['queen'].keys()):
    print((row,board['queen'][row]))

def free(i,j):
  return(board['row'][i] == 0 and board['col'][j] == 0 and
          board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0) #possible when no side is attacked

def addqueen(i,j): #addition of queen to the row
  board['queen'][i] = j
  board['row'][i] = 1
  board['col'][j] = 1
  board['nwtose'][j-i] = 1
  board['swtone'][j+i] = 1

def undoqueen(i,j): #undo steps
  board['queen'][i] = -1 #frees queen square and resets all its attacked squares
  board['row'][i] = 0
  board['col'][j] = 0
  board['nwtose'][j-i] = 0
  board['swtone'][j+i] = 0

def placequeen(i):
  n = len(board['queen'].keys())
  for j in range(n):
    if free(i,j): #check availability
      addqueen(i,j)
      if i == n-1:
        return(True)  # placement of the last queen
      else:
        extendsoln = placequeen(i+1)
      if extendsoln:
        return(True) #will be true when all queens placed
      else:
        undoqueen(i,j) # end not reached, backtrack
  else:
    return(False)

board = {}
n =6
initialize(n)
if placequeen(0):
  printboard()
