# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
df = DataFrame(columns=["a", "b", "c"])
result = df.pivot(index="a", columns="b", values="c")
expected = DataFrame(index=[], columns=[])
tm.assert_frame_equal(result, expected, check_names=False)
