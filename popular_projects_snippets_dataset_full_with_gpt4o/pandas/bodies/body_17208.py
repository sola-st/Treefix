# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH#3962
data = {
    "index": ["A", "B", "C", "C", "B", "A"],
    "columns": ["One", "One", "One", "Two", "Two", "Two"],
    "values": [1.0, 2.0, 3.0, 3.0, 2.0, 1.0],
}

frame = DataFrame(data).set_index("index")
result = frame.pivot(columns="columns", values="values")
expected = DataFrame(
    {
        "One": {"A": 1.0, "B": 2.0, "C": 3.0},
        "Two": {"A": 1.0, "B": 2.0, "C": 3.0},
    }
)

expected.index.name, expected.columns.name = "index", "columns"
tm.assert_frame_equal(result, expected)

# omit values
result = frame.pivot(columns="columns")

expected.columns = MultiIndex.from_tuples(
    [("values", "One"), ("values", "Two")], names=[None, "columns"]
)
expected.index.name = "index"
tm.assert_frame_equal(result, expected, check_names=False)
assert result.index.name == "index"
assert result.columns.names == (None, "columns")
expected.columns = expected.columns.droplevel(0)
result = frame.pivot(columns="columns", values="values")

expected.columns.name = "columns"
tm.assert_frame_equal(result, expected)
