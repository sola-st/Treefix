# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH#24206

index = MultiIndex(
    [CategoricalIndex(["A", "B"]), CategoricalIndex(["a", "b"])], codes
)
data = {"col": range(len(index))}
df = DataFrame(data=data, index=index)

expected = DataFrame(
    {
        "level_0": Categorical.from_codes(codes[0], categories=["A", "B"]),
        "level_1": Categorical.from_codes(codes[1], categories=["a", "b"]),
        "col": range(4),
    }
)

res = df.reset_index()
tm.assert_frame_equal(res, expected)

# roundtrip
res = expected.set_index(["level_0", "level_1"]).reset_index()
tm.assert_frame_equal(res, expected)
