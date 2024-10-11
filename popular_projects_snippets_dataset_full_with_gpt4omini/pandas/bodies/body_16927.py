# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
arr1 = np.zeros((2,), dtype=("i4,f4,a10"))
arr1[:] = [(1, 2.0, "Hello"), (2, 3.0, "World")]

arr2 = np.zeros((3,), dtype=("i4,f4,a10"))
arr2[:] = [(3, 4.0, "foo"), (5, 6.0, "bar"), (7.0, 8.0, "baz")]

df1 = DataFrame(arr1)
df2 = DataFrame(arr2)

result = df1._append(df2, ignore_index=True)
expected = DataFrame(np.concatenate((arr1, arr2)))
tm.assert_frame_equal(result, expected)
