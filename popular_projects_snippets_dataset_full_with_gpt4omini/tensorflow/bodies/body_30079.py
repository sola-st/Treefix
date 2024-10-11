# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
mask = True
tensor = 1
with self.cached_session():
    with self.assertRaisesRegex(ValueError, "mask.*scalar"):
        self.evaluate(array_ops.boolean_mask(tensor, mask))
