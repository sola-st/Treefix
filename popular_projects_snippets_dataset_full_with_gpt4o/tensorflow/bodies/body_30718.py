# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
tensor = [1, 2]
shift = 1
axis = 1
with self.cached_session():
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "is out of range"):
        manip_ops.roll(tensor, shift, axis).eval()
