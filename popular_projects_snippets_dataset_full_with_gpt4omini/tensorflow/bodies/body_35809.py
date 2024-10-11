# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
for attr in functools.WRAPPER_ASSIGNMENTS:
    self.assertEqual(
        getattr(variables.Variable.__add__, attr),
        getattr(ops.Tensor.__add__, attr))
