# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.assertRaisesRegex(TypeError, "not allowed in Graph"):
    for _ in variables.Variable(0.0):
        pass
with self.assertRaisesRegex(TypeError, "not allowed in Graph"):
    for _ in variables.Variable([0.0, 1.0]):
        pass
