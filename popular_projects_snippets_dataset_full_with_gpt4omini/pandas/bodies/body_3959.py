# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# https://github.com/pandas-dev/pandas/issues/37115
df = DataFrame(
    {
        "a": ["A", "A", "B"],
        "b": ["ca", "cb", "cb"],
        "v": [10] * 3,
    }
).set_index(["a", "b"])

# add another int column to get 2 blocks
df["is_"] = 1
if not using_array_manager:
    assert len(df._mgr.blocks) == 2

result = df.unstack("b")
result[("is_", "ca")] = result[("is_", "ca")].fillna(0)

expected = DataFrame(
    [[10.0, 10.0, 1.0, 1.0], [np.nan, 10.0, 0.0, 1.0]],
    index=Index(["A", "B"], dtype="object", name="a"),
    columns=MultiIndex.from_tuples(
        [("v", "ca"), ("v", "cb"), ("is_", "ca"), ("is_", "cb")],
        names=[None, "b"],
    ),
)
if using_array_manager:
    # INFO(ArrayManager) with ArrayManager preserve dtype where possible
    expected[("v", "cb")] = expected[("v", "cb")].astype("int64")
    expected[("is_", "cb")] = expected[("is_", "cb")].astype("int64")
tm.assert_frame_equal(result, expected)
