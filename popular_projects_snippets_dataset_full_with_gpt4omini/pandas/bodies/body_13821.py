# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# Test the class names and displayed value are correct on rendering MI names
df = DataFrame(
    {"A": [1, 2]},
    index=MultiIndex.from_arrays(
        [["a", "a"], [0, 1]], names=["idx_level_0", "idx_level_1"]
    ),
)
result = df.style._translate(True, True)
head = result["head"][1]
expected = [
    {
        "class": "index_name level0",
        "display_value": "idx_level_0",
        "is_visible": True,
    },
    {
        "class": "index_name level1",
        "display_value": "idx_level_1",
        "is_visible": True,
    },
    {
        "class": "blank col0",
        "display_value": blank_value,
        "is_visible": True,
    },
]
for i, expected_dict in enumerate(expected):
    assert expected_dict.items() <= head[i].items()
