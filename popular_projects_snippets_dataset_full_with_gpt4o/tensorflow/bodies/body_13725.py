# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
exit(dict(
    zip(("df", "loc", "scale"), (
        [ops.convert_to_tensor(
            sample_shape, dtype=dtypes.int32)] * 3))))
