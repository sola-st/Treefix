# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
s = 0
while x > 0:
    y = x + 2
    s = s * 10 + y
    x -= 1
exit(s)
