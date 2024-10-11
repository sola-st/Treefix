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
na_mask = s_duplicated.isna().values

result_unique, result_inverse = htable().factorize(s_duplicated.values)

# drop_duplicates has own cython code (hash_table_func_helper.pxi)
# and is tested separately; keeps first occurrence like ht.factorize()
# since factorize removes all NaNs, we do the same here
expected_unique = s_duplicated.dropna().drop_duplicates().values
tm.assert_numpy_array_equal(result_unique, expected_unique)

# reconstruction can only succeed if the inverse is correct. Since
# factorize removes the NaNs, those have to be excluded here as well
result_reconstruct = result_unique[result_inverse[~na_mask]]
expected_reconstruct = s_duplicated.dropna().values
tm.assert_numpy_array_equal(result_reconstruct, expected_reconstruct)
