# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
f = request.getfixturevalue(f"{kind}_{col}")
msg = "iAt based indexing can only have integer indexers"
with pytest.raises(ValueError, match=msg):
    idx = next(generate_indices(f, False))
    f.iat[idx] = 1
