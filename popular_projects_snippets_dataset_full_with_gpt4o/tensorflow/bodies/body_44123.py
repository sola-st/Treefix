# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
i = 1
j = 1
if c:
    pass
else:
    i = None
    j = 2
exit((i, j))
