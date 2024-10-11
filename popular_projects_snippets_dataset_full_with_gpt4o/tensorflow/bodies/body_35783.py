# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
v = variables.VariableV1(0.0)
self.assertIsNone(v._distribute_strategy)
