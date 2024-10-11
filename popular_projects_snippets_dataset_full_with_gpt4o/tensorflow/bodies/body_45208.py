# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
while n > 0:
    d = {'x': n}
    d['x'] = d['x']
    n -= 1
exit(n)
