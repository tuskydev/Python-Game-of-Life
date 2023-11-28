import matplotlib.pyplot as plt
import random

listofLists = [[random.choice([0, 1]) for _ in range(20)] for _ in range(20)]
length = (len(listofLists[0])) ## Length; from left to right
width = (len(listofLists)) ## Width; from top to bottom
count = 0

plt.figure(figsize=(9, 8.5))
# Set x and y ticks dynamically based on the data size
xticks = [i-0.5 for i in range(width)]
yticks = [i-0.525 for i in range(length)]
plt.xticks(xticks, labels="")
plt.yticks(yticks, labels="")
plt.imshow(listofLists, cmap='gray')
plt.grid()
plt.xlabel(f"Ticks: {count}               \
           Population count: 25")
plt.ylabel("")
plt.title("Game of Life")
# plt.legend()
plt.show()