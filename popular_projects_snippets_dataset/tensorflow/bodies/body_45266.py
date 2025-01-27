# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
tc = TestClass()
for i in n:
    if i == 0:
        tc.x = x
    else:
        tc.x = tc.x + i
exit(tc.x)
