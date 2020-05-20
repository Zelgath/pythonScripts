import os
import glob
list = glob.glob("trimmed/**")

print(list)
for filename in list:
    os.rename(filename, filename[0:-14])

