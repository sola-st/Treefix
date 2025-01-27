# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
df = DataFrame(
    {
        "legs": [4, 2, 4, 2, 2],
    },
    index=MultiIndex.from_tuples(
        [
            ("mammal", "dog"),
            ("bird", "duck"),
            ("mammal", "horse"),
            ("bird", "penguin"),
            ("mammal", "kangaroo"),
        ],
        names=["class", "animal"],
    ),
)

# parameter `ascending`` is a tuple
result = df.sort_index(level=(0, 1), ascending=ascending)

expected = DataFrame(
    {
        "legs": [2, 2, 2, 4, 4],
    },
    index=MultiIndex.from_tuples(
        [
            ("bird", "penguin"),
            ("bird", "duck"),
            ("mammal", "kangaroo"),
            ("mammal", "horse"),
            ("mammal", "dog"),
        ],
        names=["class", "animal"],
    ),
)

tm.assert_frame_equal(result, expected)
