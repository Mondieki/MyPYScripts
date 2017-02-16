import os
import shutil

root_src_dir = r'#'                                                 #Path to Source Directory
root_dst_dir = '#'                                                  #Location Of Back up directory

"""Merge directories if they already exist. If they don't make them. """
for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)        #Merge the folders if they already exist.
    if not os.path.exists(dst_dir):                                 #Create the folder if it doesn't exist.
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):                                #If the file alreaddy exists, overwrite it with the new copied file.
            os.remove(dst_file)                                     #Delete the old file
        shutil.move(src_file, dst_dir)                              #Copy the new file unliminet

print("Files and folders have been moved successfully!")