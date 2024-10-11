# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
try:
    raise ValueError()
except ValueError:
    x = 1
if i == 0:
    x = i - 1
exit(x)
