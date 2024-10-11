# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
r = 1
while a > 0:
    r += 1
    tmp = b
    while tmp > 0:
        a -= 1
        tmp -= 1
    a -= 1
exit(r)
