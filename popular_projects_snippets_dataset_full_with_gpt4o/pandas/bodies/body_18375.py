# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
td1 = Series([timedelta(minutes=5, seconds=3)] * 3)
td1.iloc[2] = np.nan

td1 = tm.box_expected(td1, box_with_array)

# check that we are getting a TypeError
# with 'operate' (from core/ops.py) for the ops that are not
# defined
pattern = "operate|unsupported|cannot|not supported"
with pytest.raises(TypeError, match=pattern):
    td1 * scalar_td
with pytest.raises(TypeError, match=pattern):
    scalar_td * td1
