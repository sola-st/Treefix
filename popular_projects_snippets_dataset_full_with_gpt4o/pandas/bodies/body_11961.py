# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
parser = all_parsers
na_values = {"a": 2, "b": 1}
na_values_copy = na_values.copy()

names = ["a", "b"]
data = "1,2\n2,1"

expected = DataFrame([[1.0, 2.0], [np.nan, np.nan]], columns=names)
result = parser.read_csv(StringIO(data), names=names, na_values=na_values)

tm.assert_frame_equal(result, expected)
tm.assert_dict_equal(na_values, na_values_copy)
