# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# these are explicitly allowed incompat merges, that pass thru
# the result type is dependent on if the values on the rhs are
# inferred, otherwise these will be coerced to object

df1 = DataFrame({"A": df1_vals})
df2 = DataFrame({"A": df2_vals})

result = merge(df1, df2, on=["A"])
assert is_object_dtype(result.A.dtype)
result = merge(df2, df1, on=["A"])
assert is_object_dtype(result.A.dtype)
