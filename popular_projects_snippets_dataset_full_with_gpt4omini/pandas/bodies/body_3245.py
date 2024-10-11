# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_nlargest.py
# GH#46589
df = pd.DataFrame(
    {
        "a": [1, 2, 3, 4, 5, None, 7],
        "b": [7, 6, 5, 4, 3, 2, 1],
        "c": [1, 1, 2, 2, 3, 3, 3],
    },
    index=range(7),
)
result = df.nsmallest(5, columns=["a", "b"])
expected = pd.DataFrame(
    {
        "a": [1, 2, 3, 4, 5],
        "b": [7, 6, 5, 4, 3],
        "c": [1, 1, 2, 2, 3],
    },
    index=range(5),
).astype({"a": "float"})
tm.assert_frame_equal(result, expected)
