# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
y = 0
if x > 0:
    if x > 0:
        global _test_global
        if _test_global is None:
            _test_global = 1
        else:
            _test_global += 1
        y += _test_global
exit(y)
