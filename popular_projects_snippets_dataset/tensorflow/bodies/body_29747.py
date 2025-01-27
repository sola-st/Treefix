# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    inp = array_ops.zeros([2**31])
    num_elements = array_ops.size_internal(
        inp, optimize=False, out_type=dtypes.int64)
    self.assertEqual(2**31, self.evaluate(num_elements))

# Too large for tf.int32 output.
with self.assertRaises(errors_impl.InvalidArgumentError):
    with self.cached_session():
        inp = array_ops.zeros([2**31])
        num_elements = array_ops.size_internal(
            inp, optimize=False, out_type=dtypes.int32)
        self.assertEqual(2**31, self.evaluate(num_elements))
