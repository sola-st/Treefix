# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr = create_mgr(
    "int: int; float: float; complex: complex;"
    "str: object; bool: bool; obj: object; dt: datetime",
    item_shape=(3,),
)
mgr.iset(5, np.array([1, 2, 3], dtype=np.object_))

numeric = mgr.get_numeric_data()
tm.assert_index_equal(numeric.items, Index(["int", "float", "complex", "bool"]))
tm.assert_almost_equal(
    mgr.iget(mgr.items.get_loc("float")).internal_values(),
    numeric.iget(numeric.items.get_loc("float")).internal_values(),
)

# Check sharing
numeric.iset(
    numeric.items.get_loc("float"),
    np.array([100.0, 200.0, 300.0]),
    inplace=True,
)
if using_copy_on_write:
    tm.assert_almost_equal(
        mgr.iget(mgr.items.get_loc("float")).internal_values(),
        np.array([1.0, 1.0, 1.0]),
    )
else:
    tm.assert_almost_equal(
        mgr.iget(mgr.items.get_loc("float")).internal_values(),
        np.array([100.0, 200.0, 300.0]),
    )

numeric2 = mgr.get_numeric_data(copy=True)
tm.assert_index_equal(numeric.items, Index(["int", "float", "complex", "bool"]))
numeric2.iset(
    numeric2.items.get_loc("float"),
    np.array([1000.0, 2000.0, 3000.0]),
    inplace=True,
)
if using_copy_on_write:
    tm.assert_almost_equal(
        mgr.iget(mgr.items.get_loc("float")).internal_values(),
        np.array([1.0, 1.0, 1.0]),
    )
else:
    tm.assert_almost_equal(
        mgr.iget(mgr.items.get_loc("float")).internal_values(),
        np.array([100.0, 200.0, 300.0]),
    )
