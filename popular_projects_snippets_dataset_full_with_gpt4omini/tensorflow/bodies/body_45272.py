# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
tr = self.transform(
    f, (break_statements, continue_statements, control_flow))
self.assertEqual(f(*inputs), tr(*inputs))
