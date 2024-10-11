# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
if ops.inside_function():
    self.assertFalse(inner_self.inside_function_tested)
    inner_self.inside_function_tested = True
else:
    self.assertFalse(inner_self.graph_mode_tested)
    inner_self.graph_mode_tested = True
