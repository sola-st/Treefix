# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
z = 0
if x > 0:
    if y > 0:
        z = x + y
exit(z)
