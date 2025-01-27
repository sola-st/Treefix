# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
i = 0
if c:
    j = 1
else:
    j = 2
    i = j + 1
exit(i)
