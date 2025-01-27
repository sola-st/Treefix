# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
frame = multiindex_dataframe_random_data

unstacked = frame.unstack()
assert unstacked.index.name == "first"
assert unstacked.columns.names == ["exp", "second"]

restacked = unstacked.stack()
assert restacked.index.names == frame.index.names
