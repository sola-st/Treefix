# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
df = DataFrame(
    {
        "day": {0: "sat", 1: "sun"},
        "flavour": {0: "strawberry", 1: "strawberry"},
        "sales": {0: 10, 1: 12},
        "year": {0: 2008, 1: 2008},
    }
).set_index(["year", "flavour", "day"])
result = df.xs("sat", level="day", drop_level=False)
expected = df[:1]
tm.assert_frame_equal(result, expected)

result = df.xs((2008, "sat"), level=["year", "day"], drop_level=False)
tm.assert_frame_equal(result, expected)
