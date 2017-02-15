import shutil
import os
source = os.listdir(r"C:\Audio")
destination = os.chdir(r"C:\\AudioBackUp")#print (os.listdir(destination))
for folders in source:
    shutil.move(os.path.join(source, destination))

            

