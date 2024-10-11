# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_test.py
s = 0
while x > 0:
    x -= 1
    if x % 2 > 0:
        break
    s += x
exit(s)
