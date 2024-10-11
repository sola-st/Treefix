# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
if n > 0:
    n = n + 1
    raise ValueError()
exit(n)
