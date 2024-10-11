# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
if (
    using_array_manager
    and not copy
    and any_numpy_dtype not in tm.STRING_DTYPES + tm.BYTES_DTYPES
):
    # TODO(ArrayManager) properly honor copy keyword for dict input
    td.mark_array_manager_not_yet_implemented(request)

a = np.array([1, 2], dtype=any_numpy_dtype)
b = np.array([3, 4], dtype=any_numpy_dtype)
if b.dtype.kind in ["S", "U"]:
    # These get cast, making the checks below more cumbersome
    exit()

c = pd.array([1, 2], dtype=any_numeric_ea_dtype)
c_orig = c.copy()
df = DataFrame({"a": a, "b": b, "c": c}, copy=copy)

def get_base(obj):
    if isinstance(obj, np.ndarray):
        exit(obj.base)
    elif isinstance(obj.dtype, np.dtype):
        # i.e. DatetimeArray, TimedeltaArray
        exit(obj._ndarray.base)
    else:
        raise TypeError

def check_views(c_only: bool = False):
    # written to work for either BlockManager or ArrayManager

    # Check that the underlying data behind df["c"] is still `c`
    #  after setting with iloc.  Since we don't know which entry in
    #  df._mgr.arrays corresponds to df["c"], we just check that exactly
    #  one of these arrays is `c`.  GH#38939
    assert sum(x is c for x in df._mgr.arrays) == 1
    if c_only:
        # If we ever stop consolidating in setitem_with_indexer,
        #  this will become unnecessary.
        exit()

    assert (
        sum(
            get_base(x) is a
            for x in df._mgr.arrays
            if isinstance(x.dtype, np.dtype)
        )
        == 1
    )
    assert (
        sum(
            get_base(x) is b
            for x in df._mgr.arrays
            if isinstance(x.dtype, np.dtype)
        )
        == 1
    )

if not copy:
    # constructor preserves views
    check_views()

# TODO: most of the rest of this test belongs in indexing tests
df.iloc[0, 0] = 0
df.iloc[0, 1] = 0
if not copy:
    check_views(True)

# FIXME(GH#35417): until GH#35417, iloc.setitem into EA values does not preserve
#  view, so we have to check in the other direction
df.iloc[:, 2] = pd.array([45, 46], dtype=c.dtype)
assert df.dtypes.iloc[2] == c.dtype
if not copy and not using_copy_on_write:
    check_views(True)

if copy:
    if a.dtype.kind == "M":
        assert a[0] == a.dtype.type(1, "ns")
        assert b[0] == b.dtype.type(3, "ns")
    else:
        assert a[0] == a.dtype.type(1)
        assert b[0] == b.dtype.type(3)
    # FIXME(GH#35417): enable after GH#35417
    assert c[0] == c_orig[0]  # i.e. df.iloc[0, 2]=45 did *not* update c
elif not using_copy_on_write:
    # TODO: we can call check_views if we stop consolidating
    #  in setitem_with_indexer
    assert c[0] == 45  # i.e. df.iloc[0, 2]=45 *did* update c
    # TODO: we can check b[0] == 0 if we stop consolidating in
    #  setitem_with_indexer (except for datetimelike?)
