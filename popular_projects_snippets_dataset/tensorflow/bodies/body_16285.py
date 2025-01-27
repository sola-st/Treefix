# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py
exit(ragged_factory_ops.constant(
    [
        [3, 1, 4, 1],
        [],
        [5, 9, 2],
        [6],
        [],
        [3, 1, 4, 1],
        [3, 1],
        [2, 1, 4, 1],
    ],
    dtype=dtypes.int64,
))
