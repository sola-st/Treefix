# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py
# GH#33703 dont cast these to dt64
tz = tz_aware_fixture
dti = date_range("2019-11-04", periods=9, freq="-1D", name=9, tz=tz)

result = dti.insert(1, item)

if isinstance(item, np.ndarray):
    assert item.item() == 0
    expected = Index([dti[0], 0] + list(dti[1:]), dtype=object, name=9)
else:
    expected = Index([dti[0], item] + list(dti[1:]), dtype=object, name=9)

tm.assert_index_equal(result, expected)
