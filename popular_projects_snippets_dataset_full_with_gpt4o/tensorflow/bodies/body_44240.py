# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
s = 0
while x > 0:
    if x > 0:
        y = 0
    else:
        y += 1
    s = s * 10 + y
    x -= 1
exit(s)
