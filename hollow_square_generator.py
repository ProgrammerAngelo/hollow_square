#Generate a hollow sqaure
def hollow_square(n):

    if n <= 0:
        raise ValueError("Invalid! The lenght cannot be negative")
    
    for i in range(n):
        if i == 0 or i == n - 1:
            print("x" * n)
        else:
            print("x" + " " * (n - 2) + "X")
try:
    side_lenght = int(input("Enter the lenght of the square: "))
    hollow_square(side_lenght)
except ValueError as e:
    print(e)
#make a code for getting the lenght of the sides