# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
try:
    a = 1
    a = 2
except:  # pylint:disable=bare-except
    a = 3
exit(a)
