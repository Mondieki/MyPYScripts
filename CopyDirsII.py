# Runs on Python 3
import os, time, sys, ctypes, time, datetime, shutil

#Create Backup directory and its subfolders "FM" and "Logs"
back_up_location=r'C:\Users\user_account\Documents'
os.chdir(back_up_location)
subfolder_names = ['FM','Logs']
for subfolder_name in subfolder_names:
    os.makedirs(os.path.join('BackupFolderName', subfolder_name), exist_ok=True)

no_of_copy=1
#An infinite while loop that backups up the audio after every 8 hours
while no_of_copy==1:
    #Declaring the source and destination locations of the directorires, escapes the string literals
    root_src_dir=r'C:\audio'
    root_dst_dir=r'C:\Users\user_account\Documents\BackupFolderName\FM'

    #Create text log files
    def createLogFile():
        dateofExec=time.ctime()
        datePart=dateofExec.strip()[4:]
        datePrx=datetime.datetime.strptime(datePart, "%b %d %H:%M:%S %Y")
        logfilename=str(datePrx.day)+"-"+str(datePrx.month)+"-" +str(datePrx.year)
        logdetails=str(dateofExec.strip()[8:-14]) + " " + str(dateofExec.strip()[4:-17]) + " " + str(dateofExec.strip()[20:]) + " :: Files were copied on  "+str(dateofExec) + "\n\n"
        location=r"C:\Users\user_account\Documents\BackupFolderName\Logs\\"+logfilename+".log"
        # Check if it's Python 2.X or Python 3.X
        try:
            f=open(location.encode('string-escape'),'a')
        except:
            f=open(location.encode('unicode-escape'),'a')
        f.write(logdetails)
        f.close()
    
    createLogFile()

    for src_dir, dirs, files in os.walk(root_src_dir):
        #Exclude Filestime.bin file
        files = [file for file in files if not file.endswith('.bin')]
        #Merge folders in case of a conflict.
        dst_dir=src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists (dst_dir):
            os.makedirs(dst_dir)
        # Replace the existing files with the newest files.
        for file_ in files:
            src_file = os.path.join (src_dir, file_)
            dst_file = os.path.join (dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_file)
    #Time (in seconds) to delay the operation
    time.sleep(15)
