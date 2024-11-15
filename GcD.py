# GREATEST COMMON DIVISOR PROGRAM

# z = x % y (if z is zero then the GCM is y)

x = int(input("Enter number for  x: "))  #user will decide the number of x.
y = int(input("Enter number for  y: "))  #user will decide the number of y.
while y != 0:                            # we continue repeats as long as  y is not 0.
    z = x % y                            # we calculate the remainder of x and y by dividing them.
    x, y = y, z                              # replace x with the value of y and the value of y with the value of z.(the remainder)
                                         

print("The Greatest  Common Divisor  is:", x)
