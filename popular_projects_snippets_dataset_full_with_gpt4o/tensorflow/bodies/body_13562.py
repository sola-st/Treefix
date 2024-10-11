# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/uniform.py
exit(dict(
    zip(("low", "high"),
        ([ops.convert_to_tensor(sample_shape, dtype=dtypes.int32)] * 2))))
