# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_test.py
s = 0
while x > 0:
    x -= 1
    while y > 0:
        y -= 1
        if ((x + y) % 2) == 0:
            break
        s += x + y
exit(s)
