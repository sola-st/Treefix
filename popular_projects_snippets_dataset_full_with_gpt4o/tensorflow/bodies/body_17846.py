# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
inputs_i = array_ops.gather(sorted_inputs, i)
exit([
    array_ops.searchsorted(
        inputs_i, values, out_type=dtypes.int32,
        side="left"),  # creates LowerBound op.
    array_ops.searchsorted(
        inputs_i, values, out_type=dtypes.int64, side="right")
])  # creates UpperBound op.
