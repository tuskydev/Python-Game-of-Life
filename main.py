import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import random

"""
Rules:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation.
  Similarly, all other dead cells stay dead.
"""

# listofLists = [[1, 0], [1, 1]]
listofLists = [[random.choice([0, 1]) for _ in range(15)] for _ in range(15)]
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

  # Extract columns based on cell's position
  if cell[0] > 0: # Top wall
    prevRow = lists[cell[0]-1]
  if cell[0]+1 <= row-1: # Bottom wall
    nextRow = lists[cell[0]+1]

  # Extract columns based on cell's position
  if cell[1] == 0: # Left wall
    prevRow = prevRow[:2]
    currRow = currRow[1:2]
    nextRow = nextRow[:2]
  elif cell[1] == column-1: # Right wall
    prevRow = prevRow[cell[1]-1:column]
    currRow = currRow[cell[1]-1:column-1]
    nextRow = nextRow[cell[1]-1:column]
  else: # Cell is in the middle
    prevRow = prevRow[cell[1]-1:cell[1]+2]
    currRow = currRow[cell[1]-1:cell[1]+2:2]
    nextRow = nextRow[cell[1]-1:cell[1]+2]

  return sum(prevRow) + sum(currRow) + sum(nextRow)

def update(lists):
  """
  Updates the game by one tick

  Parameters:
  - lists (list): a list of lists

  Returns:
  updatedList (list): a list of lists
  """
  global tick
  tick += 1
  updatedList = lists

  for rowIndex, list in enumerate(lists):
    for colIndex, _ in enumerate(list):
      cell = (rowIndex, colIndex)
      neighbors = getLiveNeighbors(lists, cell)

      # Cells with fewer than two live neighbours dies
      if neighbors < 2:
        updatedList[rowIndex][colIndex] = 0
      # Cells with fewer than two live neighbours dies
      elif neighbors == 2 and updatedList[rowIndex][colIndex] == 1:
        updatedList[rowIndex][colIndex] == 1
      # Cells with exactly three live neighbours becomes a live cell
      elif neighbors == 3:
        updatedList[rowIndex][colIndex] = 1
      # Cells with more than three live neighbours dies
      elif neighbors > 3:
        updatedList[rowIndex][colIndex] = 0

  return updatedList

def plotGame(ax, lists):
  ax.set_xlabel(f"Ticks: {tick}\
              Population count: {getPopCount(lists)}")

def animate():
  global listofLists

  _, ax = plt.subplots(figsize=(9, 8.5))
  xticks = [i - 0.5 for i in range(column)]
  yticks = [i - 0.51 for i in range(row)]
  ax.set_xticks(xticks)
  ax.set_xticklabels(labels="")
  ax.set_yticks(yticks)
  ax.set_yticklabels(labels="")
  ax.grid()
  ax.set_ylabel("")
  ax.set_title("Game of Life")
  legendHandles = [plt.Line2D([0], [0], marker="s", markersize=12, markerfacecolor="#000000",
                              color="w", label="Black= Alive"),
                  plt.Line2D([0], [0], marker="s", markersize=12, markerfacecolor="#ffffff",
                              color="k", label="White = Dead")]
  ax.legend(handles=legendHandles, loc="upper right")
  img = ax.imshow(listofLists, cmap=ListedColormap(['#ffffff', '#000000']))

  while getPopCount(listofLists) > 0:
    listofLists = update(listofLists)
    ax.set_xlabel(f"Ticks: {tick}       \
                  Population count: {getPopCount(listofLists)}")
    img.set_data(listofLists)
    plt.pause(0.01)

animate()
plt.show()