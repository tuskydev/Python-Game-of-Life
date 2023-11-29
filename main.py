import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random

# listofLists = [[1, 1], [1, 1]]
listofLists = [[random.choice([0, 1]) for _ in range(20)] for _ in range(20)]
length = (len(listofLists[0])) ## Length; from left to right
width = (len(listofLists)) ## Width; from top to bottom
count = 0

## Implement populationCount function
def populationCount(lists):
  counter = 0

  for list in lists:
    counter += sum(list)

  return counter

print(populationCount(listofLists))











plt.figure(figsize=(9, 8.5))
# Set x and y ticks dynamically based on the data size
xticks = [i-0.5 for i in range(width)]
yticks = [i-0.525 for i in range(length)]
plt.xticks(xticks, labels="")
plt.yticks(yticks, labels="")
plt.imshow(listofLists, cmap=ListedColormap(['#000000', '#ffffff']))
plt.grid()
plt.xlabel(f"Ticks: {count}               \
           Population count: 1000")
plt.ylabel("")
plt.title("Game of Life")
legendHandles = [plt.Line2D([0], [0], color="w", marker="s", markersize=12, markerfacecolor="#000000", label="Black= Alive"),
                 plt.Line2D([0], [0], color="k", marker="s", markersize=12, markerfacecolor="#ffffff", label="White = Dead")]
plt.legend(handles=legendHandles, loc="upper right")
plt.show()