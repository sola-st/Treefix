# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_quantile.py
# GH 28662, GH 33200, GH 33569
df = DataFrame({"key": key, "val": val})

expected = DataFrame(
    expected_val, index=Index(expected_key, name="key"), columns=["val"]
)

grp = df.groupby("key")

result = grp.quantile(0.5)
tm.assert_frame_equal(result, expected)

result = grp.quantile()
tm.assert_frame_equal(result, expected)
