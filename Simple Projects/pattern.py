while True:
  print("\n===== Make Pattern =====")
  print("1. Right Triangle")
  print("2. Diamond")
  print("3. Butterfly")
  print("4. Hollow Square")

  try:
    pattern = int(input("Choose A Pattern You Wanna Make (1-4): "))
  except ValueError:
    print("\n>>> Please select the valid menu.")
    continue

  if pattern == 1:
    print("\nRight Triangle")
    n = int(input("The row size pattern: "))
    for i in range(1, n + 1):
      for j in range(1, i + 1):
        print("*", end=" ")
      print()
    if input("Try another pattern? (y/n): ") != "y": 
      print("G'bye!")
      break
      
  elif pattern == 2:
    print("\nDiamond")
    n = int(input("The row size pattern: "))
    for i in range(2 * n - 1):
      for j in range(2 * n - 1):
        h = i if i < n else 2 * n -2 - i
        if n - 1 - h <= j <= n - 1 + h:
          print("*", end=" ")
        else:
          print(" ", end=" ")
      print()
    if input("Try another pattern? (y/n): ") != "y": 
          print("G'bye!")
          break

  elif pattern == 3:
    print("\nButterfly")
    try: 
      n = int(input("The row size pattern: "))
    except ValueError:
      print("\n>>> Please input the valid number.")
      continue
    for i in range(2 * n - 1):
      for j in range(2 * n - 1):
        h = i if i < n else 2 * n - 2 - i
        if j <= h or j >= 2 * n - 2 - h:
          print("*", end=" ")
        else:
          print(" ", end=" ")
      print()
    if input("Try another pattern? (y/n): ") != "y": 
          print("G'bye!")
          break

  elif pattern == 4:
    print("\nHollow Square")
    try:
      n = int(input("The row size pattern: "))
    except ValueError:
      print("\n>>> Please input the valid number.")
      continue
    for i in range(n):
      for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
          print("*", end=" ")
        else:
          print(" ", end=" ")
      print()
    if input("Try another pattern? (y/n): ") != "y": 
      print("G'bye!")
      break