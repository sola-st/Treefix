# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# see gh-14068
msg = "Overflow in int64 addition"
m = np.iinfo(np.int64).max
n = np.iinfo(np.int64).min

with pytest.raises(OverflowError, match=msg):
    algos.checked_add_with_arr(np.array([m, m]), m)
with pytest.raises(OverflowError, match=msg):
    algos.checked_add_with_arr(np.array([m, m]), np.array([m, m]))
with pytest.raises(OverflowError, match=msg):
    algos.checked_add_with_arr(np.array([n, n]), n)
with pytest.raises(OverflowError, match=msg):
    algos.checked_add_with_arr(np.array([n, n]), np.array([n, n]))
with pytest.raises(OverflowError, match=msg):
    algos.checked_add_with_arr(np.array([m, n]), np.array([n, n]))
with pytest.raises(OverflowError, match=msg):
    algos.checked_add_with_arr(
        np.array([m, m]), np.array([m, m]), arr_mask=np.array([False, True])
    )
with pytest.raises(OverflowError, match=msg):
    algos.checked_add_with_arr(
        np.array([m, m]), np.array([m, m]), b_mask=np.array([False, True])
    )
with pytest.raises(OverflowError, match=msg):
    algos.checked_add_with_arr(
        np.array([m, m]),
        np.array([m, m]),
        arr_mask=np.array([False, True]),
        b_mask=np.array([False, True]),
    )
with pytest.raises(OverflowError, match=msg):
    algos.checked_add_with_arr(np.array([m, m]), np.array([np.nan, m]))

# Check that the nan boolean arrays override whether or not
# the addition overflows. We don't check the result but just
# the fact that an OverflowError is not raised.
algos.checked_add_with_arr(
    np.array([m, m]), np.array([m, m]), arr_mask=np.array([True, True])
)
algos.checked_add_with_arr(
    np.array([m, m]), np.array([m, m]), b_mask=np.array([True, True])
)
algos.checked_add_with_arr(
    np.array([m, m]),
    np.array([m, m]),
    arr_mask=np.array([True, False]),
    b_mask=np.array([False, True]),
)
