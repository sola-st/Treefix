# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
if context.executing_eagerly():
    error_message = r"Attempt to convert a value \(None\)"
else:
    error_message = "None values not supported."
with self.assertRaisesRegex(ValueError, error_message):
    du.rotate_transpose(None, 1)
for x in (np.ones(1), np.ones((2, 1)), np.ones((3, 2, 1))):
    for shift in np.arange(-5, 5):
        y = du.rotate_transpose(x, shift)
        self.assertAllEqual(
            self._np_rotate_transpose(x, shift), self.evaluate(y))
        self.assertAllEqual(np.roll(x.shape, shift), y.get_shape().as_list())
