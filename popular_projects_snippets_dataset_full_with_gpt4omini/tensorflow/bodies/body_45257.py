# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

z = 5
if condition:
    x.b = 7
    z = 13

exit((x.b, z))
