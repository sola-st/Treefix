# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_dict.py
# GH#18529
# Test new columns parameter for from_dict that was added to make
# from_items(..., orient='index', columns=[...]) easier to replicate
result = DataFrame.from_dict(
    OrderedDict([("A", [1, 2]), ("B", [4, 5])]),
    orient="index",
    columns=["one", "two"],
)
expected = DataFrame([[1, 2], [4, 5]], index=["A", "B"], columns=["one", "two"])
tm.assert_frame_equal(result, expected)

msg = "cannot use columns parameter with orient='columns'"
with pytest.raises(ValueError, match=msg):
    DataFrame.from_dict(
        {"A": [1, 2], "B": [4, 5]},
        orient="columns",
        columns=["one", "two"],
    )
with pytest.raises(ValueError, match=msg):
    DataFrame.from_dict({"A": [1, 2], "B": [4, 5]}, columns=["one", "two"])
