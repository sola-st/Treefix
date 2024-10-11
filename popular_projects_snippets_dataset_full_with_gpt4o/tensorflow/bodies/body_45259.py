# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
s1 = 0
s2 = 0
for e in l:
    s1 += e
    s2 += e * e
exit((s1, s2))
