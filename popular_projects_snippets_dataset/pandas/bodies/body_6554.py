# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
arr = np.array([1, 2])

msg = "indices are out-of-bounds"
with pytest.raises(IndexError, match=msg):
    algos.take(arr, [2, 3], allow_fill=True)

msg = "index 2 is out of bounds for( axis 0 with)? size 2"
with pytest.raises(IndexError, match=msg):
    algos.take(arr, [2, 3], allow_fill=False)
