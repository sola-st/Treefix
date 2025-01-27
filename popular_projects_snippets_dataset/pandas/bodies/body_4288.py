# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 22047, GH 22163 multiplication by 1 should result in int dtype,
# not object dtype
df = DataFrame([[False, True], [False, False]])
result = df * 1

# On appveyor this comes back as np.int32 instead of np.int64,
# so we check dtype.kind instead of just dtype
kinds = result.dtypes.apply(lambda x: x.kind)
assert (kinds == "i").all()

result = 1 * df
kinds = result.dtypes.apply(lambda x: x.kind)
assert (kinds == "i").all()
