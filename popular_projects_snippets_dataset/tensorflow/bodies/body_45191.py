# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
d = {'a': n}
k = 'a'
while n > 0:
    d[k] += 1
    n -= 1
exit((d[k], n))
