# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
base = np.zeros(len(normal_lines[0].get_data()[1]))
for nl, sl in zip(normal_lines, stacked_lines):
    base += nl.get_data()[1]  # get y coordinates
    sy = sl.get_data()[1]
    tm.assert_numpy_array_equal(base, sy)
