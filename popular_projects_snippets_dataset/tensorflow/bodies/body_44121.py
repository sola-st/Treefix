# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
i = 0
j = 1
if c:
    i = None
    j = 2
exit((i, j))
