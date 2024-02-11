L1 = float(input("Enter the length of L 1: "))
L2 = float(input("Enter the length of L 2: "))
L3 = float(input("Enter the length of L 3: "))
if L1 == L2 == L3:
    print("Equilateral triangle")
elif L1 == L2 or L1 == L3 or L2 == L3:
    print("Isoceles triangle")
else:
    print("Scalene triangle")