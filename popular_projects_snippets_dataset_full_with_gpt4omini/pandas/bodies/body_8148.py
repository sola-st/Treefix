# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_npfuncs.py
# GH#14042
indices = date_range("2016-01-01 00:00:00+0200", freq="S", periods=10)
result = np.split(indices, indices_or_sections=[])[0]
expected = indices._with_freq(None)
tm.assert_index_equal(result, expected)
