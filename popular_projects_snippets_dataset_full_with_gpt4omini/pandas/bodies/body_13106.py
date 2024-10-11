# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# GH#39695
df = DataFrame({"A": [0, 1], "B": [10, 11]})
df.to_excel(path, columns=["A", "B", "A"], index=False)

result = pd.read_excel(path)
expected = DataFrame([[0, 10, 0], [1, 11, 1]], columns=["A", "B", "A.1"])
tm.assert_frame_equal(result, expected)
