# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
# Create an empty scalar where the static shape is unknown.
zeros_length_1 = array_ops.zeros(
    random_ops.random_uniform([1], minval=0, maxval=1, dtype=dtypes.int32),
    dtype=dtypes.int32)
scalar = array_ops.zeros(zeros_length_1)
with self.cached_session():
    with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                                'out of bounds'):
        self.evaluate(sort_ops.sort(scalar))
