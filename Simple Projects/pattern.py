print("\nDiamond")
def diamond(n):
  for i in range(2 * n - 1):
    for j in range(2 * n - 1):
      h = i if i < n else 2 * n -2 - i
      if n - 1 - h <= j <= n - 1 + h:
        print("*", end="")
      else:
        print(" ", end="")
    print()
print(diamond(5))

print("\nRight Triangle")
def rightTriangle(n):
  for i in range(n):
    for j in range(n):
      if j <= i:
        print("*", end="")
      else:
        print(" ", end="")
    print()
print(rightTriangle(5))