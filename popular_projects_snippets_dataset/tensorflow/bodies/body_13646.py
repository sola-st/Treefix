# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
exit(dict(
    zip(("loc", "scale"), ([ops.convert_to_tensor(
        sample_shape, dtype=dtypes.int32)] * 2))))
