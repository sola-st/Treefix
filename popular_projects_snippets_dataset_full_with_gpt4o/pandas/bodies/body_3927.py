# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# see gh-30740
df = DataFrame(
    {
        "name": ["Alice", "Bob"],
        "score": [9.5, 8],
        "employed": [False, True],
        "kids": [0, 0],
        "gender": ["female", "male"],
    }
)
df = df.set_index(["name", "employed", "kids", "gender"])
df = df.unstack(["gender"], fill_value=0)
expected = df.unstack("employed", fill_value=0).unstack("kids", fill_value=0)
result = df.unstack(["employed", "kids"], fill_value=0)
expected = DataFrame(
    [[9.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 8.0]],
    index=Index(["Alice", "Bob"], name="name"),
    columns=MultiIndex.from_tuples(
        [
            ("score", "female", False, 0),
            ("score", "female", True, 0),
            ("score", "male", False, 0),
            ("score", "male", True, 0),
        ],
        names=[None, "gender", "employed", "kids"],
    ),
)
tm.assert_frame_equal(result, expected)
