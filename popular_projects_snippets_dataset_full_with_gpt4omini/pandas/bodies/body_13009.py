# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# copied from read_csv
result = pd.read_excel("test_decimal" + read_ext, decimal=",", skiprows=1)
expected = DataFrame(
    [
        [1, 1521.1541, 187101.9543, "ABC", "poi", 4.738797819],
        [2, 121.12, 14897.76, "DEF", "uyt", 0.377320872],
        [3, 878.158, 108013.434, "GHI", "rez", 2.735694704],
    ],
    columns=["Id", "Number1", "Number2", "Text1", "Text2", "Number3"],
)
tm.assert_frame_equal(result, expected)
