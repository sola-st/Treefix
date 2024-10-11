# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
exit(dict(
    zip(("concentration", "rate"), ([ops.convert_to_tensor(
        sample_shape, dtype=dtypes.int32)] * 2))))
