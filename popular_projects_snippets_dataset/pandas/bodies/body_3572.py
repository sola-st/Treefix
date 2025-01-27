# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
frame = multiindex_dataframe_random_data

frame.index.names = ["first", "second"]
result = frame.sort_index(level="second")
expected = frame.sort_index(level=1)
tm.assert_frame_equal(result, expected)
