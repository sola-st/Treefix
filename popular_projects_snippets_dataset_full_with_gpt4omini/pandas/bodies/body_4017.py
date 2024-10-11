# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
# from numpy documentation
arr = np.zeros((2,), dtype=("i4,f4,a10"))
arr[:] = [(1, 2.0, "Hello"), (2, 3.0, "World")]

# TODO(wesm): unused
frame = DataFrame.from_records(arr)  # noqa

index = Index(np.arange(len(arr))[::-1])
indexed_frame = DataFrame.from_records(arr, index=index)
tm.assert_index_equal(indexed_frame.index, index)

# without names, it should go to last ditch
arr2 = np.zeros((2, 3))
tm.assert_frame_equal(DataFrame.from_records(arr2), DataFrame(arr2))

# wrong length
msg = "|".join(
    [
        r"Length of values \(2\) does not match length of index \(1\)",
    ]
)
with pytest.raises(ValueError, match=msg):
    DataFrame.from_records(arr, index=index[:-1])

indexed_frame = DataFrame.from_records(arr, index="f1")

# what to do?
records = indexed_frame.to_records()
assert len(records.dtype.names) == 3

records = indexed_frame.to_records(index=False)
assert len(records.dtype.names) == 2
assert "index" not in records.dtype.names
