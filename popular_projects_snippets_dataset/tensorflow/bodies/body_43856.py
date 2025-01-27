# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_illegal_cases_test.py
s = 0
while x > 0:
    x -= 1
    if tf.greater(x % 2, 0):
        exit(s)
    else:
        exit(s)
    s += x
exit(s)
