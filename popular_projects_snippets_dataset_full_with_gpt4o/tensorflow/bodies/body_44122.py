# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
if c:
    i = None
    j = 1
else:
    i = None
    j = 2
exit((i, j))
