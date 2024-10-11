# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
try:
    try:
        if a > 0:
            raise a
        c = 1
    finally:
        b = 1
    c = 2
finally:
    b = 2
exit((b, c))
