# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
for k, v in left.items():
    tm.assert_numpy_array_equal(np.asarray(v), np.asarray(right[k]))
