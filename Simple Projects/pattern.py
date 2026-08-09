print("\n===== Make Pattern =====")
print("1. Right Triangle")
print("2. Diamond")
print("3. Butterfly")
print("4. Hollow Square")

pattern = int(input("Choose A Pattern You Wanna Make (1-4): "))

rows = int(input("The row size pattern: "))
for i in range(1, rows + 1):
  for j in range(1, i + 1):
    print("*", end=" ")
  print()

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

print("\nButterfly")
def butterfly(n):
  for i in range(2 * n - 1):
    for j in range(2 * n - 1):
      h = i if i < n else 2 * n - 2 - i
      if j <= h or j >= 2 * n - 2 - h:
        print("*", end="")
      else:
        print(" ", end="")
    print()
print(butterfly(5))

print("\nHollow Square")
def hollow_square(n):
  for i in range(n):
    for j in range(n):
      if i == 0 or i == n-1 or j == 0 or j == n-1:
        print("*", end="")
      else:
        print(" ", end="")
    print()
print(hollow_square(5))