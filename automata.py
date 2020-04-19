from math import floor
from random import randint

from PIL import Image, ImageDraw

rules = [18, 22, 26, 30, 45, 57, 60, 62, 73, 75, 82, 86, 89, 90, 101, 102, 105, 109, 110, 124, 126, 129, 131, 135, 137,
         145, 146, 149, 150, 153, 154, 161, 165, 167, 181, 182, 190, 193, 195, 210, 214, 218, 225]

rulesetNo = rules[randint(0, len(rules) - 1)]
ruleset = list(map(int, bin(rulesetNo)[2:].zfill(8)[::-1]))

for i in range(0, 8):
    if ruleset[i] == 1:
        if randint(0, 100) <= 25:
            ruleset[i] = 2

print(ruleset)

width = 400
height = 300

cellSize = randint(1, 5)
rectSize = cellSize - 1

visibleGenerations = floor(height / cellSize)
numCells = floor(width / cellSize)
cells = [0] * numCells

centre = floor(len(cells) / 2)

print("Width: %s, Height %s, Visible Generations: %s, Cells: %s, Centre: %s" %
      (width, height, visibleGenerations, numCells, centre))

cells[randint(0, numCells - 1)] = 1

img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

for generation in range(0, visibleGenerations * 2):

    previousCells = cells.copy()

    for cell in range(0, numCells):
        leftIndex = cell - 1
        if leftIndex < 0:
            leftIndex = numCells - 1
        rightIndex = cell + 1
        if rightIndex >= numCells:
            rightIndex = 0

        left = previousCells[leftIndex]
        leftRule = 0
        if left >= 1:
            leftRule = 1

        middle = previousCells[cell]
        middleRule = 0
        if middle >= 1:
            middleRule = 1

        right = previousCells[rightIndex]
        rightRule = 0
        if right >= 1:
            rightRule = 1

        result = ruleset[int("%s%s%s" % (leftRule, middleRule, rightRule), 2)]

        cells[cell] = result

    if generation >= visibleGenerations:
        newImg = img.transform(img.size, Image.AFFINE, (1, 0, 0, 0, 1, cellSize))
        img.close()
        img = newImg
        draw = ImageDraw.Draw(img)

    y = min(generation, (visibleGenerations - 1)) * cellSize

    for cell in range(0, numCells):

        x = cell * cellSize

        if cells[cell] == 1:
            draw.rectangle([(x, y), (x + rectSize, y + rectSize)], fill='black')
        elif cells[cell] == 2:
            draw.rectangle([(x, y), (x + rectSize, y + rectSize)], fill='red')
        else:
            draw.rectangle([(x, y), (x + rectSize, y + rectSize)], fill='white')

img.save("example.png")
# img.show()
