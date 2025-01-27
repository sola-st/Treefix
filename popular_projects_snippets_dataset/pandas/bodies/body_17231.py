# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies_basic.loc[2, "col2_c"] = np.nan
with pytest.raises(
    ValueError, match=r"Dummy DataFrame contains NA value in column: 'col2_c'"
):
    from_dummies(dummies_basic, sep="_")
