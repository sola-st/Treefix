# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
x = []
with self.assertRaisesRegex(ValueError, r"elems must be a Tensor or"):
    _ = map_fn.map_fn(lambda e: e, x)
