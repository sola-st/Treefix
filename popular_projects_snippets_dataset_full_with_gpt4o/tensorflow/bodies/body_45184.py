# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
i = 0
s = 0
while i < n:
    s += i
    i += 1
exit((s, i, n))
