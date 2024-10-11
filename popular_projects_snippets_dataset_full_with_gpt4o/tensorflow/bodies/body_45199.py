# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
d = {}
while n < 5:
    if n == 0:
        d['subkey'] = x
    else:
        d['subkey'] = d['subkey'] + 1
    n += 1
exit(d)
