# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
rt1 = RaggedTensor.from_row_splits(
    values=x, row_splits=[0, 4, 7, 8], validate=False)
rt2 = rt1 * [[10], [100], [1000]]
exit(rt2.flat_values)
