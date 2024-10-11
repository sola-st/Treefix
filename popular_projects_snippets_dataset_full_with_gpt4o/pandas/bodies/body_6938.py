# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_engines.py
dti1 = pd.date_range("2016-01-01", periods=3)
dti2 = dti1.insert(1, pd.NaT)  # non-monotonic
dti3 = dti1.insert(3, dti1[0])  # non-unique
dti4 = pd.date_range("2016-01-01", freq="ns", periods=2_000_000)
dti5 = dti4.insert(0, dti4[0])  # over size threshold, not unique

msg = "|".join([re.escape(str(scalar)), re.escape(repr(scalar))])
for dti in [dti1, dti2, dti3, dti4, dti5]:
    with pytest.raises(TypeError, match=msg):
        scalar in dti._engine

    with pytest.raises(KeyError, match=msg):
        dti._engine.get_loc(scalar)
