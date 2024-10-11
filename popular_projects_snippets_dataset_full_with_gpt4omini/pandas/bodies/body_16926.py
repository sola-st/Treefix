# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
df = DataFrame(columns=["A", "B", "C"])
df3 = DataFrame(index=[0, 1], columns=["A", "B"])
df5 = df._append(df3, sort=sort)

expected = DataFrame(index=[0, 1], columns=["A", "B", "C"])
tm.assert_frame_equal(df5, expected)
