# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
cwd = os.getcwd()
os.chdir(temppath)
try:
    exit()
finally:
    os.chdir(cwd)
