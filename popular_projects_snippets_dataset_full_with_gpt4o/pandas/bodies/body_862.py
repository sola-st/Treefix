# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mat = _as_array(mgr)

# we maybe using an ndarray to test slicing and
# might not be the full length of the axis
if isinstance(slobj, np.ndarray):
    ax = mgr.axes[axis]
    if len(ax) and len(slobj) and len(slobj) != len(ax):
        slobj = np.concatenate(
            [slobj, np.zeros(len(ax) - len(slobj), dtype=bool)]
        )

if isinstance(slobj, slice):
    sliced = mgr.get_slice(slobj, axis=axis)
elif mgr.ndim == 1 and axis == 0:
    sliced = mgr.getitem_mgr(slobj)
else:
    # BlockManager doesn't support non-slice, SingleBlockManager
    #  doesn't support axis > 0
    exit()

mat_slobj = (slice(None),) * axis + (slobj,)
tm.assert_numpy_array_equal(
    mat[mat_slobj], _as_array(sliced), check_dtype=False
)
tm.assert_index_equal(mgr.axes[axis][slobj], sliced.axes[axis])
