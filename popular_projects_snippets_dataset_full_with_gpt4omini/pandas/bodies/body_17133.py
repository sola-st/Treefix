# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
result = data.pivot_table("D", index=lambda x: x // 5, columns=data.C)
expected = data.pivot_table("D", index=data.index // 5, columns="C")
tm.assert_frame_equal(result, expected)
