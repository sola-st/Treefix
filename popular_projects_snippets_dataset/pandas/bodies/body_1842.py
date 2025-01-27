# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

r = test_frame.resample("H")
tm.assert_index_equal(r._selected_obj.columns, test_frame.columns)

r = test_frame.resample("H")["B"]
assert r._selected_obj.name == test_frame.columns[1]

# technically this is allowed
r = test_frame.resample("H")["A", "B"]
tm.assert_index_equal(r._selected_obj.columns, test_frame.columns[[0, 1]])

r = test_frame.resample("H")["A", "B"]
tm.assert_index_equal(r._selected_obj.columns, test_frame.columns[[0, 1]])
