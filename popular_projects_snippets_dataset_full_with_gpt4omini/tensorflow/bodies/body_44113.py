# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
i = 0
j = 1
if i < n:
    i += 1
    j *= 10
exit((i, j))
