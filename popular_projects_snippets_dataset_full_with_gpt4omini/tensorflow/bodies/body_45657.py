# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
if a > 0:
    if a > 1:
        a = 1
    else:
        a = 2
else:
    if a > 2:
        a = 3
    else:
        a = 4
