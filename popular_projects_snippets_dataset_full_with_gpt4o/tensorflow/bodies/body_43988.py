# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
p = 0
while a > 0:
    tmp = b
    while tmp > 0:
        p += 1
        tmp -= 1
    a -= 1
exit(p)
