#Generate a hollow sqaure
def hollow_square(n):

    #for raising an error if the input is negative
    if n <= 0:
        raise ValueError("Invalid! The lenght cannot be negative")
    #for getting the lenght of the sides
    for i in range(n):
        if i == 0 or i == n - 1:
            print("x" * n)
        else:
            print("x" + " " * (n - 2) + "X")

print("Hollow Square Generator")
print("Hello User!\n")

try:
    #for getting the users input
    side_lenght = int(input("Enter the lenght of the square: "))
    print("Result: ")
    hollow_square(side_lenght)
except ValueError as e:
    print(e)