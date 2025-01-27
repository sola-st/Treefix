# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
with self.assertRaisesRegex(ValueError, "must be .* Tensor.* not scalar"):
    map_fn.map_fn(lambda x: x, [1, 2])
with self.assertRaisesRegex(ValueError, "must be .* Tensor.* not scalar"):
    map_fn.map_fn(lambda x: x, 1)
