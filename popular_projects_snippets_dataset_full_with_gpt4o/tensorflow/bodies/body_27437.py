# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
"""Tests that exception is raised when input is malformed.
    """
record_defaults = [
    constant_op.constant([], dtypes.int32),
    constant_op.constant([], dtypes.int64),
    constant_op.constant([], dtypes.float32),
    constant_op.constant([], dtypes.float64),
    constant_op.constant([], dtypes.string)
]

column_names = ["col%d" % i for i in range(5)]
inputs = [[",".join(x for x in column_names), "0,1,2,3,4", "5,6,7,8,9"], [
    ",".join(x for x in column_names), "10,11,12,13,14", "15,16,17,18,19"
]]
filenames = self._setup_files(inputs)

# Duplicate column names
with self.assertRaises(ValueError):
    self._make_csv_dataset(
        filenames,
        batch_size=1,
        column_defaults=record_defaults,
        label_name="col0",
        column_names=column_names * 2)

# Label key not one of column names
with self.assertRaises(ValueError):
    self._make_csv_dataset(
        filenames,
        batch_size=1,
        column_defaults=record_defaults,
        label_name="not_a_real_label",
        column_names=column_names)
