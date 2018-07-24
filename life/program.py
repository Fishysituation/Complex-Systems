import sys, pygame

dead = '.'
alive = '*'

deadColour = (40, 40, 40)
aliveColour = (255, 255, 255)


size = 0
dimensionslg = 0, 0
widthlg, heightlg = 0, 0
dimensionspx = 0, 0
widthpx, heightpx = 0, 0

board = []

#create empty board matrix
def Generate():
	for y in range(heightlg):
		line = []
		for x in range(widthlg):
			line.append(dead)
		board.append(line)

#display cmdln board
def DisplayConsole():
	print()
	for y in range(0, heightlg):
		for x in range(0, widthlg):
			print(' ' + board[y][x], end = '')
		print()
	print()

#writes console board to window
def DisplayScreen(surface):
	for y in range(0, heightlg):
		for x in range(0, widthlg):
			#if a cell is alive
			if board[x][y] == alive:
				#draw it as white square
				cell = pygame.Rect(x*size, y*size, size, size)
				surface.fill(aliveColour, rect=cell, special_flags=0)

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

	#DisplayConsole()

	pygame.init()
	
	#create SURFACE size of screen
	screen = pygame.display.set_mode(dimensionspx)
	pygame.display.set_caption('Game of Life')
	pygame.mouse.set_visible(1)

	#setup clock
	clock = pygame.time.Clock()

	while (True):

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()

		Iterate()
		#DisplayConsole()

		#draw background
		screen.fill(deadColour)
		#draw cells
		DisplayScreen(screen)
		
		pygame.display.flip()

		clock.tick(10)
		


#setup
#get dimensions
dimensions = input().split()
widthlg = int(dimensions[0])
heightlg = int(dimensions[1])
size = int(input())

dimensionspx = widthpx, heightpx = int(widthlg*size), int(heightlg*size)

#draw board
Generate()

# "left/top justified" string input 
# i.e. can enter fewer chars/lines than logical height/width
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


Main()
