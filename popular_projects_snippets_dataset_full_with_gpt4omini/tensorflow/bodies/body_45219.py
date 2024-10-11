# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
a = 0
b = 0
if n > 0:
    a = -n
else:
    b = 2 * n
exit((a, b))
