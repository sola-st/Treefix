# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies_basic.loc[2, "col2_c"] = "str"
with pytest.raises(TypeError, match=r"Passed DataFrame contains non-dummy data"):
    from_dummies(dummies_basic, sep="_")
