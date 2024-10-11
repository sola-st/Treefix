# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
d = {'a': n}
while n > 0:
    d['a'] += 1
    n -= 1
exit((d['a'], n))
