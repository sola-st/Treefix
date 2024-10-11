# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr = create_mgr(
    "int: int; float: float; complex: complex;"
    "str: object; bool: bool; obj: object; dt: datetime",
    item_shape=(3,),
)
mgr.iset(6, np.array([True, False, True], dtype=np.object_))

bools = mgr.get_bool_data()
tm.assert_index_equal(bools.items, Index(["bool"]))
tm.assert_almost_equal(
    mgr.iget(mgr.items.get_loc("bool")).internal_values(),
    bools.iget(bools.items.get_loc("bool")).internal_values(),
)

bools.iset(0, np.array([True, False, True]), inplace=True)
if using_copy_on_write:
    tm.assert_numpy_array_equal(
        mgr.iget(mgr.items.get_loc("bool")).internal_values(),
        np.array([True, True, True]),
    )
else:
    tm.assert_numpy_array_equal(
        mgr.iget(mgr.items.get_loc("bool")).internal_values(),
        np.array([True, False, True]),
    )

# Check sharing
bools2 = mgr.get_bool_data(copy=True)
bools2.iset(0, np.array([False, True, False]))
if using_copy_on_write:
    tm.assert_numpy_array_equal(
        mgr.iget(mgr.items.get_loc("bool")).internal_values(),
        np.array([True, True, True]),
    )
else:
    tm.assert_numpy_array_equal(
        mgr.iget(mgr.items.get_loc("bool")).internal_values(),
        np.array([True, False, True]),
    )
