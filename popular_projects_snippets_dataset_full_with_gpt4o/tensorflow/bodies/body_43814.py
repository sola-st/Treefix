# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
s = 0
while x > 0:
    x -= 1
    if x > y:
        break
    s += x
else:
    s = -100
exit(s)
