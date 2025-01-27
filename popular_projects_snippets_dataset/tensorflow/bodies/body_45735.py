# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
try:
    if a > 0:
        a = 1
    else:
        a = 2
except Exception1:  # pylint:disable=undefined-variable
    a = 3
a = 4
