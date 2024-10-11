# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
"""Tests that datasets can be created from CSV files with no header line.
    """
record_defaults = [
    constant_op.constant([], dtypes.int32),
    constant_op.constant([], dtypes.int64),
    constant_op.constant([], dtypes.float32),
    constant_op.constant([], dtypes.float64),
    constant_op.constant([], dtypes.string)
]

column_names = ["col%d" % i for i in range(5)]
inputs = [["0,1,2,3,4", "5,6,7,8,9"], ["10,11,12,13,14", "15,16,17,18,19"]]
expected_output = [[0, 1, 2, 3, b"4"], [5, 6, 7, 8, b"9"],
                   [10, 11, 12, 13, b"14"], [15, 16, 17, 18, b"19"]]
label = "col0"

self._test_dataset(
    inputs,
    expected_output=expected_output,
    expected_keys=column_names,
    column_names=column_names,
    label_name=label,
    batch_size=1,
    num_epochs=1,
    shuffle=False,
    header=False,
    column_defaults=record_defaults,
)
