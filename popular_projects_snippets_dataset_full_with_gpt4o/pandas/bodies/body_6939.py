# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_engines.py
tdi1 = pd.timedelta_range("42 days", freq="9h", periods=1234)
tdi2 = tdi1.insert(1, pd.NaT)  # non-monotonic
tdi3 = tdi1.insert(3, tdi1[0])  # non-unique
tdi4 = pd.timedelta_range("42 days", freq="ns", periods=2_000_000)
tdi5 = tdi4.insert(0, tdi4[0])  # over size threshold, not unique

msg = "|".join([re.escape(str(scalar)), re.escape(repr(scalar))])
for tdi in [tdi1, tdi2, tdi3, tdi4, tdi5]:
    with pytest.raises(TypeError, match=msg):
        scalar in tdi._engine

    with pytest.raises(KeyError, match=msg):
        tdi._engine.get_loc(scalar)
