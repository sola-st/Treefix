# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
tc = TestClassX(TestClassY({'z': TestClassX(n)}))
if n > 0:
    while n > 0:
        if n < 2:
            tc.x.y['z'].x += 1
        n -= 1
exit((n, tc))
