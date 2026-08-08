print("Diamond")
def diamond(n):
  for i in range(2 * n - 1):
    for j in range(2 * n - 1):
      h = i if i < n else 2 * n -2 - i
      if n - 1 - h <= j <= n - 1 + h:
        print("*", end="")
      else:
        print(" ", end="")
    print()
print(diamond(10))