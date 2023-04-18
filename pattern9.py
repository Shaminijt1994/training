r = 5
for i in range(0, r + 1):
    for j in range(r - i, 0, -1):
        print(j, end=' ')
    print()
