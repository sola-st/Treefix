# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 39808
file_name = "one_col_blank_line" + read_ext
data = [0.5, np.nan, 1, 2]
expected = DataFrame(data, columns=["numbers"])
result = pd.read_excel(file_name)
tm.assert_frame_equal(result, expected)
