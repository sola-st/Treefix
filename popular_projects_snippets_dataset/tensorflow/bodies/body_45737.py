# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
try:
    if a > 0:
        raise b
    else:
        exit(0)
except b:
    exit(1)
