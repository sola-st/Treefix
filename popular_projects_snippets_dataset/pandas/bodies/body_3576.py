# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH#23452
df = DataFrame(
    {"foo": range(len(categories))},
    index=CategoricalIndex(
        data=categories, categories=categories, ordered=True
    ),
)
df.index = df.index.reorder_categories(df.index.categories[::-1])
result = df.sort_index()
expected = DataFrame(
    {"foo": reversed(range(len(categories)))},
    index=CategoricalIndex(
        data=categories[::-1], categories=categories[::-1], ordered=True
    ),
)
tm.assert_frame_equal(result, expected)
