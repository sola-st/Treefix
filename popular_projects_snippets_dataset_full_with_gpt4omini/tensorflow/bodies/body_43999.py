# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
x = type_x(x)
y = type_x(y)
self.assertFunctionMatchesEager(independent_ifs, x, y)
