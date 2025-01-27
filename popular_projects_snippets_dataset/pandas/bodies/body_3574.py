# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
frame = multiindex_dataframe_random_data

result = frame.sort_index()
assert result.index.names == frame.index.names
