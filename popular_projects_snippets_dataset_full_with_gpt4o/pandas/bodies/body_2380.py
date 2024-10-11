# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_coercion.py
# GH#18415 Setting values in a single column preserves dtype,
#  while setting them in multiple columns did unwanted cast.

# Note that A here has 2 blocks, below we do the same thing
#  with a consolidated frame.
A = DataFrame(np.zeros((6, 5), dtype=np.float32))
A = pd.concat([A, A], axis=1, keys=[1, 2])
if consolidate:
    A = A._consolidate()

A.loc[2:3, (1, slice(2, 3))] = np.ones((2, 2), dtype=np.float32)
assert (A.dtypes == np.float32).all()

A.loc[0:5, (1, slice(2, 3))] = np.ones((6, 2), dtype=np.float32)

assert (A.dtypes == np.float32).all()

A.loc[:, (1, slice(2, 3))] = np.ones((6, 2), dtype=np.float32)
assert (A.dtypes == np.float32).all()
