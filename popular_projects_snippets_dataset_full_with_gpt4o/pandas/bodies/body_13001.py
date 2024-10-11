# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
"""
        For various parameters, we should get the same result whether we
        limit the rows during load (nrows=3) or after (df.iloc[:3]).
        """
# GH 46894
expected = pd.read_excel(
    filename + read_ext,
    sheet_name=sheet_name,
    header=header,
    index_col=index_col,
    skiprows=skiprows,
).iloc[:3]
actual = pd.read_excel(
    filename + read_ext,
    sheet_name=sheet_name,
    header=header,
    index_col=index_col,
    skiprows=skiprows,
    nrows=3,
)
tm.assert_frame_equal(actual, expected)
