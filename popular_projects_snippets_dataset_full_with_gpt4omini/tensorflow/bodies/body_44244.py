# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
i = 7
s = 0
for i in fn(n):
    s = s * 10 + i
exit((i, s))
