# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
try:
    a = 1
finally:
    a = 2
exit(a)
