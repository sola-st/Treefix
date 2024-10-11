# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
y = 0
if x > 0:
    y = -2 * x
    if y > 0:
        x = -3 * x
else:
    y = 4 * x
exit((x, y))
