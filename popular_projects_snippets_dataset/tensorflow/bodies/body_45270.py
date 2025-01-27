# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
s = constant_op.constant(list(range(n)))
for _ in l:
    s += constant_op.constant([a for a in range(n)])
exit(s)
