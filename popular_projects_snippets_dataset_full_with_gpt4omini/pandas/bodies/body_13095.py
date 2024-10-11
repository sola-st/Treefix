# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# Re issue #18735
# Test that pd.read_excel ignores commented lines at the end of file

df = DataFrame({"a": ["1", "#2"], "b": ["2", "3"]})
df.to_excel(path, index=False)

# Test that all-comment lines at EoF are ignored
expected = DataFrame({"a": [1], "b": [2]})
result = pd.read_excel(path, comment="#")
tm.assert_frame_equal(result, expected)
