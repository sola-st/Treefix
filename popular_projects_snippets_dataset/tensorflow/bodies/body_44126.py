# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
i = 0
j = 2
if c:
    j = j + 1
    i = j + 1
exit(i)
