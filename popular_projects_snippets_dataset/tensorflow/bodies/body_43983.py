# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
y = 0
if x > 0:
    if x < 3:
        y = -2 * x
        x = -3 * x
exit((x, y))
