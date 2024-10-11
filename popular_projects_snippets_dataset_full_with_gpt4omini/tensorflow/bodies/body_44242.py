# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
while x > 0:
    y = x + 2
    x -= 1
exit(y)
