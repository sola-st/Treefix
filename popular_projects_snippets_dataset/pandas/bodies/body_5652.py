# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# output of maker has guaranteed unique elements
maker = getattr(tm, "make" + tm_dtype + "Index")
s = Series(maker(1000))
if htable == ht.Float64HashTable:
    # add NaN for float column
    s.loc[500] = np.nan
elif htable == ht.PyObjectHashTable:
    # use different NaN types for object column
    s.loc[500:502] = [np.nan, None, NaT]

# create duplicated selection
s_duplicated = s.sample(frac=3, replace=True).reset_index(drop=True)
s_duplicated.values.setflags(write=writable)

# drop_duplicates has own cython code (hash_table_func_helper.pxi)
# and is tested separately; keeps first occurrence like ht.unique()
expected_unique = s_duplicated.drop_duplicates(keep="first").values
result_unique = htable().unique(s_duplicated.values)
tm.assert_numpy_array_equal(result_unique, expected_unique)

# test return_inverse=True
# reconstruction can only succeed if the inverse is correct
result_unique, result_inverse = htable().unique(
    s_duplicated.values, return_inverse=True
)
tm.assert_numpy_array_equal(result_unique, expected_unique)
reconstr = result_unique[result_inverse]
tm.assert_numpy_array_equal(reconstr, s_duplicated.values)
