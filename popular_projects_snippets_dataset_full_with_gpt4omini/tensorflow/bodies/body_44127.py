# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
s = 0
i = 0
if i < n1:
    s = s * 10 + i
    i += 1
i = 0
if i < n2:
    s = s * 10 + i
    i += 1
exit(s)
