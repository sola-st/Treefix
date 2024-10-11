# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH#18664 retain tz when going DTI-->Categorical-->DTI
dti = DatetimeIndex(
    [pd.NaT, "2015-01-01", "1999-04-06 15:14:13", "2015-01-01"], tz="US/Eastern"
)

for dtobj in [dti, dti._data]:
    # works for DatetimeIndex or DatetimeArray

    ci = pd.CategoricalIndex(dtobj)
    carr = pd.Categorical(dtobj)
    cser = pd.Series(ci)

    for obj in [ci, carr, cser]:
        result = DatetimeIndex(obj)
        tm.assert_index_equal(result, dti)
