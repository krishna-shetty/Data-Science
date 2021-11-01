n = 5
X = [2]
stairs = [1]

def ways(n, X):
    for i in range(1, int(n) + 1):
        stairs.insert(i, 0)
        for s in X:
            if i - s >= 0:
                stairs[i] = stairs[i] + stairs[i - s]
            else:
                stairs[i] = stairs[i] + 0
    
    return stairs[-1]

print(ways(n, X))
        