# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
f = request.getfixturevalue(f"{kind}_{col}")
indices = generate_indices(f, False)
for i in indices:
    f.at[i] = 1
    expected = f.loc[i]
    tm.assert_almost_equal(expected, 1)
