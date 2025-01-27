# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
s = 0
for i in fn(n):
    s = s * 10 + i
exit((i, s))  # pylint:disable=undefined-loop-variable
