# Extracted from ./data/repos/pandas/pandas/tests/window/test_api.py
frame = DataFrame(np.random.randn(5, 5))
r = frame.rolling(window=5, step=step)
tm.assert_index_equal(r._selected_obj.columns, frame[::step].columns)

r = frame.rolling(window=5, step=step)[1]
assert r._selected_obj.name == frame[::step].columns[1]

# technically this is allowed
r = frame.rolling(window=5, step=step)[1, 3]
tm.assert_index_equal(r._selected_obj.columns, frame[::step].columns[[1, 3]])

r = frame.rolling(window=5, step=step)[[1, 3]]
tm.assert_index_equal(r._selected_obj.columns, frame[::step].columns[[1, 3]])
