import os.path
import time
 
# Infinite loop
while 1:
    time.sleep(1)
    os.system('clear')
    # In0 is user input line to determine which directory to check for (Must use "/root" not "~")
    In0 = input("What directory/file would you like to check?: ")
    # X is variable that contains returned value - True/False(1/0) for user defined variable "In0"
    X = os.path.exists(In0)
    Y = "DIRECTORY RETURNED: TRUE"
    Z = "DIRECTORY RETURNED: FALSE"
    Made = "- DIRECTORY MADE"
    y = "OKAY"
    n = " - ABORTED"
    R = ", REMOVING - "
    # If directory exists
    if X > 0:
        time.sleep(1)
        os.system('clear')
        # Print Y As defined above
        print(Y)
        time.sleep(3)
        # Asks if we would like to remove the pre-existing directory
        In1 = input("Would you like to remove the directory - "+In0+"- Y/N?: ")
        if In1 == 'Y' or In1 == 'y':
            os.system('clear')
            # If YES (Y/y), remove directory
            os.rmdir(In0)
            print(y,R,In0)
            time.sleep(1)
            continue
        else:
           # ELSE
            os.system('clear')
            # Print y+In0+n as defined above
            print(y,R,In0,n)
            time.sleep(3)
            # ELSE Continue loop from start
            continue
 
    # If directory does not exist
    else:
        time.sleep(1)
        os.system('clear')
        # Asks if we would like to make a new directory
        print(Z)
        In1 = input("Would you like to make a new directory - "+In0+" - Y/N?: ")
        if In1 == 'Y' or In1 == 'y':
            # If YES (Y/y), Make the new directory as defined by In0
            os.system('clear')
            os.mkdir(In0)
            time.sleep(1)
            os.system('clear')
            # Print y+In0+Made as defined above
            print(y,In0,Made)
            time.sleep(3)
            # Continue main loop from start
            continue
        # Otherwise
        else:
            os.system('clear')
            # Print y+In0+n as defined above
            print(y,In0,n)
            time.sleep(3)
            # Continue main loop from start
            continue
    continue