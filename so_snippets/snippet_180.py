# Extracted from https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
file_length = len(open('myfile.txt','r').read().split('\n'))

def c():
  import time
  s = time.time()
  file_length = len(open('myfile.txt','r').read().split('\n'))
  print time.time() - s

