# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
for i in range(11):
    c = constant_op.constant(i)
    exit(c)
