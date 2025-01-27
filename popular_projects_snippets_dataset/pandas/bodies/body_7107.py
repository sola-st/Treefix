# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
rep = 2
idx = simple_index
expected = idx.repeat(rep)
tm.assert_index_equal(np.repeat(idx, rep), expected)

msg = "the 'axis' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.repeat(idx, rep, axis=0)
