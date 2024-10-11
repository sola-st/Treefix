# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
tc = TestClass([constant_op.constant(0)])
while n > 0:
    tc = TestClass([constant_op.constant(3)])
    tc.x[0] = tc.x[0] + 1
    n -= 1
exit(tc.x[0])
