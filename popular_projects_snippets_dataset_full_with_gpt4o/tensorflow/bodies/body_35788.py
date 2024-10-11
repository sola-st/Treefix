# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.assertRaisesRegex(TypeError, "scalar tensor"):
    for _ in variables.Variable(0.0):
        pass
values = []
for v in variables.Variable([0.0, 1.0]):
    values.append(v)
self.assertAllClose([0., 1.], values)
