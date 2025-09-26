

# Get first 5 letters
letters = list(string.ascii_uppercase[:5])  # ['A','B','C','D','E']
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print(letters[i], end=" ")  # use row letter
        else:
            print(" ", end=" ")
    print()