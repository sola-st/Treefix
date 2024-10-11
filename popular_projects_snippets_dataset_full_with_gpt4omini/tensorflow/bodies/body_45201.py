# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
d = {}
while n < 5:
    k = 'subkey'
    d[k] = x + 1
    n += 1
exit(d)
