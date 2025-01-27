# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
y = [a, b]
while y[1] <= 10:
    y[0] += 1
    y[1] *= 2
exit(y)
