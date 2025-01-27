# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with context.eager_mode():
    var = variables.Variable(np.zeros(shape=[1, 1]))
    with self.assertRaisesRegex(ValueError, "shape.*and.*are incompatible"):
        var.assign(np.zeros(shape=[2, 2]))
