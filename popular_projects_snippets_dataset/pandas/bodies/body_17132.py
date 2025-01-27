# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
result = data.pivot_table("D", index=data.A, columns=data.C)
expected = data.pivot_table("D", index="A", columns="C")
tm.assert_frame_equal(result, expected)
