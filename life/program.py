import sys, pygame
pygame.init()

dead = '.'
alive = '*'


size = 40
dimensionslg = widthlg, heightlg = 10, 20
dimensionspx = widthpx, heightpx = int(widthlg*size), int(heightlg*size)


board = []

#create empty board matrix
def Generate():
	for y in range(heightlg):
		line = []
		for x in range(widthlg):
			line.append(dead)
		board.append(line)


#get board input
def GetIn():
	# "left/top justified" string input 
	# i.e. can enter fewer chars than logical height/width
	starting = []
	for i in range(0, heightlg):
		stringIn = input()
		if stringIn == 'stop':
			break
		else:
			starting.append(stringIn)

	#apply the starting board state
	for y in range(0, len(starting)):
		for x in range(0, len(starting[y])):
			board[y][x] = starting[y][x]


#display cmdln board
def Display():
	print()
	for y in range(0, heightlg):
		for x in range(0, widthlg):
			print(' ' + board[y][x], end = '')
		print()
	print()

#wraps board around in horzintal direction
def modX(num):
	if num >= 0:
		return num % widthlg
    #if negative, check other side of board
	else:
		return num + widthlg

#wraps board around in vertical direction
def modY(num):
	if num >= 0:
		return num % heightlg
    #if negative, check other side of board
	else:
		return num + heightlg

#Iterate the board one time step
def Iterate():
	changes = []	
	#check entire range of board
	for y in range(0, heightlg):
		for x in range(0, widthlg):
			count = 0

			#iteate through all neighbour cells
			for j in range(y-1, y+2):
				for i in range(x-1, x+2):
					if board[modY(j)][modX(i)] == alive:
						count += 1
						if j == y and i == x:
							count -= 1

			#kill loney/overpopulated
			if count > 3 or count < 2:
				changes.append((y, x, dead))
			#birth cell
			elif count == 3:
				changes.append((y, x, alive))
		
	for i in range(0, len(changes)):
		current = changes[i]
		board[current[0]][current[1]] = current[2]


#entry point
def Main():
	Generate()
	GetIn()
	Display()

	while (True):
		stringIn = input()
		if stringIn == 'n':
			Iterate()
			Display()		
		
		elif stringIn == 'quit':
			break

    #screen = pygame.display.set_mode(dimensionspx)

Main()
