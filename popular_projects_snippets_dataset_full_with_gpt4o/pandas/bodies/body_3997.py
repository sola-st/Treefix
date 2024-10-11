# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_dict.py
# GH#8425
a = OrderedDict(
    [
        ("one", OrderedDict([("col_a", "foo1"), ("col_b", "bar1")])),
        ("two", OrderedDict([("col_a", "foo2"), ("col_b", "bar2")])),
        ("three", OrderedDict([("col_a", "foo3"), ("col_b", "bar3")])),
    ]
)
expected = DataFrame.from_dict(a, orient="columns").T
result = DataFrame.from_dict(a, orient="index")
tm.assert_frame_equal(result, expected)
