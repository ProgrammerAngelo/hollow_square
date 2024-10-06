#Generate a hollow sqaure
def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("x" * n)
        else:
            print("x" + " " * (n - 2) + "X")
hollow_square(n)
#make a code for getting the lenght of the sides