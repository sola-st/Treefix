# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 4078
# construction error with mi and all-nan frame
tuples = [(2, 3), (3, 3), (3, 3)]
mi = MultiIndex.from_tuples(tuples)
df = DataFrame(index=mi, columns=mi)
assert isna(df).values.ravel().all()

tuples = [(3, 3), (2, 3), (3, 3)]
mi = MultiIndex.from_tuples(tuples)
df = DataFrame(index=mi, columns=mi)
assert isna(df).values.ravel().all()
