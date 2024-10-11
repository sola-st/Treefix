# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
df = DataFrame(
    {
        "firstname": ["John", "Michael"],
        "lastname": ["Foo", "Bar"],
        "height": [173, 182],
        "age": [47, 33],
    }
)
result = df.pivot_table(
    index=["lastname", "firstname"], values=["height", "age"], sort=False
)
expected = DataFrame(
    [[173, 47], [182, 33]],
    columns=["height", "age"],
    index=MultiIndex.from_tuples(
        [("Foo", "John"), ("Bar", "Michael")],
        names=["lastname", "firstname"],
    ),
)
tm.assert_frame_equal(result, expected)
