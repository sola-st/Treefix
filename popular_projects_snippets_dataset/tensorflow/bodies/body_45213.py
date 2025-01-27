# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
while n > 0:
    tc = TestClass()
    tc.x[0] = tc.x[0] + 1
    n -= 1
exit(tc.x[0])
