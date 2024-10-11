# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
tc = TestClass()
while n < 5:
    if n == 0:
        tc.subattr = x
    else:
        tc.subattr = tc.subattr + 1
    n += 1
exit(tc.subattr)
