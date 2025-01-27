# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
i = RangeIndex(0, name="Foo")
i_view = i.view()
assert i_view.name == "Foo"

i_view = i.view("i8")
tm.assert_numpy_array_equal(i.values, i_view)

i_view = i.view(RangeIndex)
tm.assert_index_equal(i, i_view)
