# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
Cols = Enum("Cols", "col1 col2")

q1 = DataFrame({Cols.col1: [1, 2, 3]})
q2 = DataFrame({Cols.col1: [1, 2, 3]})

result = q1[Cols.col1] == q2[Cols.col1]
expected = Series([True, True, True], name=Cols.col1)

tm.assert_series_equal(result, expected)
