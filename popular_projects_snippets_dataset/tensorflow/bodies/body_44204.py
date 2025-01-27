# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_test.py
s = 0
while x > 0:
    x -= 1
    s += x
    if x % 2 > 0:
        exit(s)
    else:
        exit(-s)
exit(s)
