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

# listofLists = [[1, 0], [1, 1]]
listofLists = [[random.choice([0, 1]) for _ in range(4)] for _ in range(4)]
row = (len(listofLists[0])) ## Left to right
column = (len(listofLists)) ## Top to bottom
tick = 0

def populationCount(lists):
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
  cellNeighbors = 0
  prevRow = []
  currRow = lists[cell[0]]
  nextRow = []

  ## If a cell is at the top wall
  if cell[0] > 0:
    prevRow = lists[cell[0]-1]
  ## If a cell is at the bottom wall
  if cell[0]+1 <= row-1:
    nextRow = lists[cell[0]+1]


  ## If a cell is at the left wall
  if cell[1] == 0:
    prevRow = prevRow[:2]
    currRow = currRow[1:2]
    nextRow = nextRow[:2]
  ## If a cell is at the right wall
  elif cell[1] == column-1:
    prevRow = prevRow[cell[1]-1:column]
    currRow = currRow[cell[1]-1:column-1]
    nextRow = nextRow[cell[1]-1:column]
  ## # If a cell is in the middle
  else:
    prevRow = prevRow[cell[1]-1:cell[1]+2]
    currRow = currRow[cell[1]-1:cell[1]+2:2]
    nextRow = nextRow[cell[1]-1:cell[1]+2]

  cellNeighbors += sum(prevRow) + sum(currRow) + sum(nextRow)

  return cellNeighbors

cell = (1, 1)
print(getLiveNeighbors(listofLists, cell))


def update():
  """
  Updates the game by one tick

  Parameters:
  -

  Returns:
  None
  """









plt.figure(figsize=(9, 8.5))
# Set x and y ticks dynamically based on the data size
xticks = [i-0.5 for i in range(column)]
yticks = [i-0.51 for i in range(row)]
plt.xticks(xticks, labels="")
plt.yticks(yticks, labels="")
plt.imshow(listofLists, cmap=ListedColormap(['#ffffff', '#000000']))
plt.grid()
plt.xlabel(f"Ticks: {tick}               \
           Population count: 1000")
plt.ylabel("")
plt.title("Game of Life")
legendHandles = [plt.Line2D([0], [0], marker="s", markersize=12, markerfacecolor="#000000",
                            color="w", label="Black= Alive"),
                 plt.Line2D([0], [0], marker="s", markersize=12, markerfacecolor="#ffffff",
                            color="k", label="White = Dead")]
plt.legend(handles=legendHandles, loc="upper right")
plt.show()