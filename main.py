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

listofLists = [[1, 2], [3, 5]]
# listofLists = [[random.choice([0, 1]) for _ in range(20)] for _ in range(20)]
length = (len(listofLists[0])) ## Length; from left to right
width = (len(listofLists)) ## Width; from top to bottom
tick = 0

def populationCount(lists):
  """
  lists: a list of lists

  Calculates how many live cells there are in the current tick

  Returns an int
  """
  counter = 0

  for list in lists:
    counter += sum(list)

  return counter

def doesClear(lists, cell):
  """
  Examines the neighboring cells of a given cell and survives if it passes rule #1.

  Parameters:
  - lists (list): a list of lists
  - cell (list[index]): list with an index indicating the position of a cell

  Returns:
  bool: True if the cell dies, False otherwise.
  """
  cellNeighbors = 0

  for list in lists:
    print("this is list", list)


# print(doesClear(listofLists, ))
print(listofLists[0][1])






def birthCell(list, ):
  """

  Returns a boolean
  """






def update():
  """

  Updates
  Returns a new list of lists holding all the cells
  """









plt.figure(figsize=(9, 8.5))
# Set x and y ticks dynamically based on the data size
xticks = [i-0.5 for i in range(width)]
yticks = [i-0.525 for i in range(length)]
plt.xticks(xticks, labels="")
plt.yticks(yticks, labels="")
plt.imshow(listofLists, cmap=ListedColormap(['#000000', '#ffffff']))
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
# plt.show()