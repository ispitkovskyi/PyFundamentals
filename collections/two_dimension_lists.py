
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print("Print element #2 in line #1:", number_grid[0][1])
print("Print element #2 in line #3:", number_grid[2][1])

print("####### Go through all elements of each array ################")
for row in number_grid:
    for col in row:
        print(col)
    print("")