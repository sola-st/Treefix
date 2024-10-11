# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
while n > 0:
    d = {'x': n}
    k = 'x'
    d[k] = d[k]
    n -= 1
exit(n)
