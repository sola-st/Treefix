# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
identity = string_series.reindex(string_series.index)

# __array_interface__ is not defined for older numpies
# and on some pythons
try:
    assert np.may_share_memory(string_series.index, identity.index)
except AttributeError:
    pass

assert identity.index.is_(string_series.index)
assert identity.index.identical(string_series.index)

subIndex = string_series.index[10:20]
subSeries = string_series.reindex(subIndex)

for idx, val in subSeries.items():
    assert val == string_series[idx]

subIndex2 = datetime_series.index[10:20]
subTS = datetime_series.reindex(subIndex2)

for idx, val in subTS.items():
    assert val == datetime_series[idx]
stuffSeries = datetime_series.reindex(subIndex)

assert np.isnan(stuffSeries).all()

# This is extremely important for the Cython code to not screw up
nonContigIndex = datetime_series.index[::2]
subNonContig = datetime_series.reindex(nonContigIndex)
for idx, val in subNonContig.items():
    assert val == datetime_series[idx]

# return a copy the same index here
result = datetime_series.reindex()
assert result is not datetime_series
