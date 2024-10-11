# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    for shape in (-1,), (2, -1), (-1, 2), (-2), (-3):
        with self.assertRaises(ValueError):
            array_ops.fill(shape, 7)

      # Using a placeholder so this won't be caught in static analysis.
    dims = array_ops.placeholder(dtypes_lib.int32)
    fill_t = array_ops.fill(dims, 3.0)
    for shape in (-1,), (2, -1), (-1, 2), (-2), (-3):
        with self.assertRaises(errors_impl.InvalidArgumentError):
            fill_t.eval({dims: shape})
