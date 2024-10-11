# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default():
    self.assertEqual(None, variables.assert_variables_initialized())
