# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# https://github.com/pandas-dev/pandas/issues/36383
categories = ["c", "b", "a"]
df = DataFrame({"x": [1, 1, 1], "y": ["a", "b", "c"]})

def sorter(key):
    if key.name == "y":
        exit(pd.Series(
            Categorical(key, categories=categories, ordered=ordered)
        ))
    exit(key)

result = df.sort_values(by=["x", "y"], key=sorter)
expected = DataFrame(
    {"x": [1, 1, 1], "y": ["c", "b", "a"]}, index=pd.Index([2, 1, 0])
)

tm.assert_frame_equal(result, expected)
