# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# issue #13292
greek = "\u0394\u03bf\u03ba\u03b9\u03bc\u03ae"
frame = DataFrame({"foo": [1, 2, 3]})
table = pivot_table(
    frame, index=["foo"], aggfunc=len, margins=True, margins_name=greek
)
index = Index([1, 2, 3, greek], dtype="object", name="foo")
expected = DataFrame(index=index, columns=[])
tm.assert_frame_equal(table, expected)
