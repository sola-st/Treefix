# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
inds = list(string_series.index[[5, 8, 12]])
string_series.loc[inds] = 5
msg = r"\['foo'\] not in index"
with pytest.raises(KeyError, match=msg):
    string_series.loc[inds + ["foo"]] = 5
