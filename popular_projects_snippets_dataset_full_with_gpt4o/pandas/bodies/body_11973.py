# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# GH#42808
parser = all_parsers
data = """0
NaN
True
False
"""
result = parser.read_csv(StringIO(data), dtype="float")
expected = DataFrame.from_dict({"0": [np.nan, 1.0, 0.0]})
tm.assert_frame_equal(result, expected)
