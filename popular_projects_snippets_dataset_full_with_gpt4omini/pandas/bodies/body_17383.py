# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py

pyarrow = import_module("pyarrow")
table = pyarrow.Table.from_pandas(df)
result = table.to_pandas()
tm.assert_frame_equal(result, df)
