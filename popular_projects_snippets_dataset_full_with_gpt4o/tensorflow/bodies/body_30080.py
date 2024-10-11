# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
mask = [True, True, True]
tensor = [[1, 2], [3, 4]]
with self.cached_session():
    with self.assertRaisesRegex(ValueError, "incompatible"):
        self.evaluate(array_ops.boolean_mask(tensor, mask))
