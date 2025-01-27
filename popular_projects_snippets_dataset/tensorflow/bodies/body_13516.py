# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
exit(dict(zip(
    ["concentration1", "concentration0"],
    [ops.convert_to_tensor(sample_shape, dtype=dtypes.int32)] * 2)))
