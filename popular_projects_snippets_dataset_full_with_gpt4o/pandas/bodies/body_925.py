# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
f = request.getfixturevalue(f"{kind}_{col}")
indices = generate_indices(f, True)
for i in indices:
    f.iat[i] = 1
    expected = f.values[i]
    tm.assert_almost_equal(expected, 1)
