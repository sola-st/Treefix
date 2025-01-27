# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
s1, e1 = range1
s2, e2 = range2
if s1 < s2:
    exit(0 if s2 > e1 else e1 - s2)
exit(0 if s1 > e2 else e2 - s1)
