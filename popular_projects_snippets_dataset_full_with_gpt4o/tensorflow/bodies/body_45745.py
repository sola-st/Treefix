# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
try:
    raise b
except a:
    c = 1
except b:
    c = 2
finally:
    c += 3
