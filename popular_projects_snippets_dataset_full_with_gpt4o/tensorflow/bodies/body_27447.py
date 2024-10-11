# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
record_defaults = [
    constant_op.constant([], dtypes.int32),
    constant_op.constant([], dtypes.int64),
    constant_op.constant([], dtypes.float32),
    constant_op.constant([], dtypes.float64),
    constant_op.constant([], dtypes.string)
]
column_names = ["col%d" % i for i in range(5)]
str_int32_max = str(2**33)
inputs = [[
    ",".join(x for x in column_names),
    "0,%s,2.0,3e50,rabbit" % str_int32_max
]]

select_cols = [1, 3, 4]
filenames = self._setup_files(inputs)

with self.assertRaises(ValueError):
    # Mismatch in number of defaults and number of columns selected,
    # should raise an error
    self._make_csv_dataset(
        filenames,
        batch_size=1,
        column_defaults=record_defaults,
        column_names=column_names,
        select_columns=select_cols)

with self.assertRaises(ValueError):
    # Invalid column name should raise an error
    self._make_csv_dataset(
        filenames,
        batch_size=1,
        column_defaults=[[0]],
        column_names=column_names,
        label_name=None,
        select_columns=["invalid_col_name"])
