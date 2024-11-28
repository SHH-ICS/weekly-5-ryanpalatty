iterations = int(input("Enter a number: "))
pi = 0

for i in range(iterations):
    pi += (-1)**i / (2 * i + 1)

print("Approximated value of PI: ", 4 * pi)
