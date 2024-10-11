# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
x = type_(x)
self.assertFunctionMatchesEager(while_with_continue_in_context_manager, x)
