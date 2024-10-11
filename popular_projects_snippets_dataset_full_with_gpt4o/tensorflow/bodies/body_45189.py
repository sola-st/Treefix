# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
tc = TestClass()
while n > 0:
    tc.x += 1
    n -= 1
exit(n)
