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
expected_output = [[0, 2**33, 2.0, 3e50, b"rabbit"]]

select_cols = [1, 3, 4]
self._test_dataset(
    inputs,
    expected_output=[[x[i] for i in select_cols] for x in expected_output],
    expected_keys=[column_names[i] for i in select_cols],
    column_names=column_names,
    column_defaults=[record_defaults[i] for i in select_cols],
    batch_size=1,
    num_epochs=1,
    shuffle=False,
    header=True,
    select_columns=select_cols,
)

# Can still do inference without provided defaults
self._test_dataset(
    inputs,
    expected_output=[[x[i] for i in select_cols] for x in expected_output],
    expected_keys=[column_names[i] for i in select_cols],
    column_names=column_names,
    batch_size=1,
    num_epochs=1,
    shuffle=False,
    header=True,
    select_columns=select_cols,
)

# Can still do column name inference
self._test_dataset(
    inputs,
    expected_output=[[x[i] for i in select_cols] for x in expected_output],
    expected_keys=[column_names[i] for i in select_cols],
    batch_size=1,
    num_epochs=1,
    shuffle=False,
    header=True,
    select_columns=select_cols,
)

# Can specify column names instead of indices
self._test_dataset(
    inputs,
    expected_output=[[x[i] for i in select_cols] for x in expected_output],
    expected_keys=[column_names[i] for i in select_cols],
    column_names=column_names,
    batch_size=1,
    num_epochs=1,
    shuffle=False,
    header=True,
    select_columns=[column_names[i] for i in select_cols],
)
