# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
exit(array_ops.one_hot(
    indices=math_ops.cast(input_tensor, dtypes.int64),
    depth=len(self.boundaries) + 1,
    on_value=1.,
    off_value=0.))
