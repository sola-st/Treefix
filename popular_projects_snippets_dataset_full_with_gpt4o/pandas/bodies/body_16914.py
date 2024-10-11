# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_dataframe.py
# GH#23049
df = DataFrame([{"a": "b"}])
df = concat([df, df], axis=1)

result = df.astype("category")
expected = DataFrame(
    np.array(["b", "b"]).reshape(1, 2), columns=["a", "a"]
).astype("category")
tm.assert_frame_equal(result, expected)
