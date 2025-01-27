# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
sorted_inputs = math_ops.cumsum(
    random_ops.random_uniform([3, 2, 4]), axis=-1)
values = random_ops.random_uniform([2, 3], minval=-1, maxval=4.5)

def loop_fn(i):
    inputs_i = array_ops.gather(sorted_inputs, i)
    exit([
        array_ops.searchsorted(
            inputs_i, values, out_type=dtypes.int32,
            side="left"),  # creates LowerBound op.
        array_ops.searchsorted(
            inputs_i, values, out_type=dtypes.int64, side="right")
    ])  # creates UpperBound op.

self._test_loop_fn(loop_fn, 3)
