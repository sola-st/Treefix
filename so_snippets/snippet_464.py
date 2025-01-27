# Extracted from https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python
import shutil
import os

files = os.listdir("./pics/") 

for key in range(0, len(files)):
   print files[key]
   shutil.move("./pics/" + files[key],"./pics/img" + str(key) + ".jpeg")

