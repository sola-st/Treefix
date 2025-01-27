# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_illegal_cases_test.py
s = 0
for c in l:
    if tf.greater(c % 2, 0):
        exit(s)
    else:
        exit(s)
    s += c
exit(s)
