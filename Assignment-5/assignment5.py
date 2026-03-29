n = 5

# 1. Square Hollow
print("\n1. Square Hollow")
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 2. Number Triangle
print("\n2. Number Triangle")
n = 4
for i in range(1, n+1):
    # spaces
    for j in range(n - i):
        print(" ", end="")
    
    # numbers
    for j in range(i):
        print(i, end=" ")
    
    print()

# 3. Increasing Pyramid
print("\n3. Increasing Pyramid")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 4. Reverse Pyramid
print("\n4. Reverse Pyramid")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 5. Changing Numbers
print("\n5. Changing Numbers")
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 6. Zero-One Triangle
print("\n6. Zero-One Triangle")
for i in range(1, n+1):
    for j in range(1, i+1):
        print((i+j)%2, end=" ")
    print()

# 7. Palindrome Triangle
print("\n7. Palindrome Triangle")
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i+1):
        print(j, end=" ")
    print()

# 8. Rhombus
print("\n8. Rhombus")
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(n):
        print("*", end=" ")
    print()

# 9. Diamond
print("\n9. Diamond")
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

# 10. Butterfly
print("\n10. Butterfly")
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    for j in range(2*(n-i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(2*(n-i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# 11. Square Fill
print("\n11. Square Fill")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# 12. Right Half Pyramid
print("\n12. Right Half Pyramid")
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

# 13. Reverse Right Half
print("\n13. Reverse Right Half")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# 14. Left Half Pyramid
print("\n14. Left Half Pyramid")
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

# 15. Reverse Left Half
print("\n15. Reverse Left Half")
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

# 16. K Pattern
print("\n16. K Pattern")
for i in range(n):
    for j in range(n):
        if j == 0 or i + j == n//2 or i - j == n//2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 17. Triangle Star
print("\n17. Triangle Star")
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

# 18. Reverse Number Triangle
print("\n18. Reverse Number Triangle")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 19. Mirror Image Triangle
print("\n19. Mirror Image Triangle")
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 20. Hollow Triangle
print("\n20. Hollow Triangle")
for i in range(1, n+1):
    for j in range(1, i+1):
        if j==1 or j==i or i==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 21. Hollow Reverse Triangle
print("\n21. Hollow Reverse Triangle")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        if j==1 or j==i or i==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 22. Hollow Diamond
print("\n22. Hollow Diamond")
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 23. Hollow Hourglass
print("\n23. Hollow Hourglass")
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(2, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 24. Pascal Triangle
print("\n24. Pascal Triangle")
for i in range(n):
    num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

# 25. Right Pascal Triangle
print("\n25. Right Pascal Triangle")
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
