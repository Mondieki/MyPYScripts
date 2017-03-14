import os, sys, time

back_up_location=r'C:\Users\mondi\Documents'
os.chdir(back_up_location)
subfolder_names = ['FM','Logs']
for subfolder_name in subfolder_names:
    os.makedirs(os.path.join('Jouvert', subfolder_name), exist_ok=True)

print(os.getcwd())