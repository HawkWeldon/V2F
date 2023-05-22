import glob
import os
os.system('cls')
def Del():
 for f in files:
    os.remove(f)
files = glob.glob('D:/Code2.0/V2frm/Op/*')
Del()
print('Done')