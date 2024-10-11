# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
df = DataFrame(np.random.randn(4, 3))
df2 = DataFrame(np.random.randint(0, 10, size=4).reshape(4, 1))
df3 = DataFrame({5: "foo"}, index=range(4))

# These are actual copies.
result = concat([df, df2, df3], axis=1, copy=True)

for arr in result._mgr.arrays:
    assert arr.base is None

# These are the same.
result = concat([df, df2, df3], axis=1, copy=False)

for arr in result._mgr.arrays:
    if arr.dtype.kind == "f":
        assert arr.base is df._mgr.arrays[0].base
    elif arr.dtype.kind in ["i", "u"]:
        assert arr.base is df2._mgr.arrays[0].base
    elif arr.dtype == object:
        if using_array_manager:
            # we get the same array object, which has no base
            assert arr is df3._mgr.arrays[0]
        else:
            assert arr.base is not None

        # Float block was consolidated.
df4 = DataFrame(np.random.randn(4, 1))
result = concat([df, df2, df3, df4], axis=1, copy=False)
for arr in result._mgr.arrays:
    if arr.dtype.kind == "f":
        if using_array_manager or using_copy_on_write:
            # this is a view on some array in either df or df4
            assert any(
                np.shares_memory(arr, other)
                for other in df._mgr.arrays + df4._mgr.arrays
            )
        else:
            # the block was consolidated, so we got a copy anyway
            assert arr.base is None
    elif arr.dtype.kind in ["i", "u"]:
        assert arr.base is df2._mgr.arrays[0].base
    elif arr.dtype == object:
        # this is a view on df3
        assert any(np.shares_memory(arr, other) for other in df3._mgr.arrays)
