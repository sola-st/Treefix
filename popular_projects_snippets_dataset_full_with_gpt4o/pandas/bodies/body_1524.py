# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#20388
np.random.seed(13)
col_data = [str(np.random.random() * 1e-12) for _ in range(5)]
result = DataFrame(col_data, columns=["A"])
expected = DataFrame(col_data, columns=["A"], dtype=object)
tm.assert_frame_equal(result, expected)

# assigning with loc/iloc attempts to set the values inplace, which
#  in this case is successful
result.loc[result.index, "A"] = [float(x) for x in col_data]
expected = DataFrame(col_data, columns=["A"], dtype=float).astype(object)
tm.assert_frame_equal(result, expected)

# assigning the entire column using __setitem__ swaps in the new array
# GH#???
result["A"] = [float(x) for x in col_data]
expected = DataFrame(col_data, columns=["A"], dtype=float)
tm.assert_frame_equal(result, expected)
