# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
obj.a = 0
obj.b = 0
if n > 0:
    obj.a = -n
else:
    obj.b = 2 * n
exit(obj)
