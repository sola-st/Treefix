# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
while x > 2:
    x /= 2
else:
    x += 1
exit(x)
