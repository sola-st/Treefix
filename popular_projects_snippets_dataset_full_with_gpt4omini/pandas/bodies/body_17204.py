# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
data = {
    "index": ["A", "B", "C", "C", "B", "A"],
    "columns": ["One", "One", "One", "Two", "Two", "Two"],
    "values": [1.0, 2.0, 3.0, 3.0, 2.0, 1.0],
}

frame = DataFrame(data)
pivoted = frame.pivot(index="index", columns="columns", values="values")

expected = DataFrame(
    {
        "One": {"A": 1.0, "B": 2.0, "C": 3.0},
        "Two": {"A": 1.0, "B": 2.0, "C": 3.0},
    }
)

expected.index.name, expected.columns.name = "index", "columns"
tm.assert_frame_equal(pivoted, expected)

# name tracking
assert pivoted.index.name == "index"
assert pivoted.columns.name == "columns"

# don't specify values
pivoted = frame.pivot(index="index", columns="columns")
assert pivoted.index.name == "index"
assert pivoted.columns.names == (None, "columns")
