# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
for data in (2, [3], 7), ([2], 3, 7), ([2], [3], 7):
    self.check(array_ops.concat, (data, 0),
               r"Can't concatenate scalars \(use tf.stack instead\)",
               [2, 3, 7])
