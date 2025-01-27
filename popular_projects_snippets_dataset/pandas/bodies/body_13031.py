# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_odf.py
# GH#45598
expected = pd.DataFrame(
    [[1.0, 4.0, 7], [np.nan, np.nan, 8], [3.0, 6.0, 9]],
    columns=["Column 1", "Column 2", "Column 3"],
)

result = pd.read_excel("test_newlines.ods")

tm.assert_frame_equal(result, expected)
