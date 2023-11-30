import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random

"""
Rules:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation.
  Similarly, all other dead cells stay dead.
"""

listofLists = [[random.choice([0, 1]) for _ in range(175)] for _ in range(175)]
row = (len(listofLists[0])) # Left to right
column = (len(listofLists)) # Top to bottom
tick = 0

def getPopCount(lists):
  """
  Calculates how many live cells there are in the current tick

  Parameters:
  - lists: a list of lists

  Returns:
  int: The sum of all living cells.
  """
  counter = 0

  for list in lists:
    counter += sum(list)

  return counter

def getLiveNeighbors(lists, cell):
  """
  Examines the neighboring cells of a given cell

  Parameters:
  - lists (list): a list of lists
  - cell (tuple): a tuple with two integers representing the (row, column) position of a cell

  Returns:
  int: The number of alive neighboring cells.
  """
  prevRow = []
  currRow = lists[cell[0]]
  nextRow = []

  if cell[0] != 0: # Top wall
    prevRow = lists[cell[0]-1]
  if cell[0]+1 != row: # Bottom wall
    nextRow = lists[cell[0]+1]

  if cell[1] == 0: # Left wall
    prevRow = prevRow[:2]
    currRow = currRow[1:2]
    nextRow = nextRow[:2]
  elif cell[1]+1 == column: # Right wall
    prevRow = prevRow[cell[1]-1:column]
    currRow = currRow[cell[1]-1:column-1]
    nextRow = nextRow[cell[1]-1:column]
  else: # Cell is in the middle
    prevRow = prevRow[cell[1]-1:cell[1]+2]
    tempCurrRow = currRow[cell[1]-1:cell[1]+2]
    currRow = [tempCurrRow[0], tempCurrRow[2]]
    nextRow = nextRow[cell[1]-1:cell[1]+2]

  return sum(prevRow) + sum(currRow) + sum(nextRow)

def update():
  """
  Updates the game by one tick

  Parameters:
  - lists (list): a list of lists

  Returns:
  updatedList (list): a list of lists
  """
  global tick, listofLists
  tick += 1
  tempList = [row[:] for row in listofLists]

  for rowIndex, list in enumerate(listofLists):
    for colIndex, _ in enumerate(list):
      cell = (rowIndex, colIndex)
      neighbors = getLiveNeighbors(listofLists, cell)

      # Cells with fewer than two live neighbours dies
      if neighbors < 2:
        tempList[rowIndex][colIndex] = 0
      # Cells with fewer than two live neighbours dies
      elif neighbors == 2 and tempList[rowIndex][colIndex] == 1:
        tempList[rowIndex][colIndex] == 1
      # Cells with exactly three live neighbours becomes a live cell
      elif neighbors == 3:
        tempList[rowIndex][colIndex] = 1
      # Cells with more than three live neighbours dies
      elif neighbors > 3:
        tempList[rowIndex][colIndex] = 0

  listofLists = [row[:] for row in tempList]

  return listofLists

def animate():
  global listofLists

  fig, ax = plt.subplots(figsize=(9,8.5))
  ax.set_ylabel("")
  ax.set_title("Game of Life")
  img = ax.imshow(listofLists, cmap=ListedColormap(['#ffffff', '#000000']))
  # Legend for alive (Black) and dead (White) cells
  legendHandles = [plt.Line2D([0], [0], marker="s", markersize=12, markerfacecolor="#000000",
                            color="w", label="Black= Alive"),
                  plt.Line2D([0], [0], marker="s", markersize=12, markerfacecolor="#ffffff",
                            color="k", label="White = Dead")]
  fig.legend(handles=legendHandles, loc="upper right")

  while getPopCount(listofLists) > 0:
    ax.set_xlabel(f"Ticks: {tick}   Population count: {getPopCount(listofLists)}")
    img.set_data(listofLists)
    update()
    plt.pause(.05)

animate()
plt.show()
