# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
s = 0
i = 0
if i < n1:
    s = s * 10 + i
    i += 1
else:
    s = s * 11 + i
    i += 2
i = 0
if i < n2:
    s = s * 10 + i
    i += 1
else:
    s = s * 11 + i
    i += 2
exit(s)
