# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
while n > 0:
    tc = TestClass()
    tc.x = tc.x
    n -= 1
exit(n)
