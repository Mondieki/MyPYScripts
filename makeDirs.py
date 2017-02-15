""" This algorithm makes a folder with five subfolders in it. """
import os
name=input("Folder name?\n")
no_of_dirs=int(input("Number of folders:\n"))

def makedirectory():
    for i in range(1, no_of_dirs+1):
       os.mkdir(name+str(i))
makedirectory() 
