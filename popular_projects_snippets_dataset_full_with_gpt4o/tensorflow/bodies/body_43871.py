# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
x = [a, 0]

if x[0] > 0:
    x[1] = 1
else:
    x[1] = -1
exit(x)
