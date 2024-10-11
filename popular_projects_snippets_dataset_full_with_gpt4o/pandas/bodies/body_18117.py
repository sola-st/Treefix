# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#13200
# different base freq
base = PeriodIndex(["2011-01", "2011-02", "2011-03", "2011-04"], freq=freq)
base = tm.box_expected(base, box_with_array)

msg = rf"Invalid comparison between dtype=period\[{freq}\] and Period"
with pytest.raises(TypeError, match=msg):
    base <= Period("2011", freq="A")

with pytest.raises(TypeError, match=msg):
    Period("2011", freq="A") >= base

# TODO: Could parametrize over boxes for idx?
idx = PeriodIndex(["2011", "2012", "2013", "2014"], freq="A")
rev_msg = r"Invalid comparison between dtype=period\[A-DEC\] and PeriodArray"
idx_msg = rev_msg if box_with_array in [tm.to_array, pd.array] else msg
with pytest.raises(TypeError, match=idx_msg):
    base <= idx

# Different frequency
msg = rf"Invalid comparison between dtype=period\[{freq}\] and Period"
with pytest.raises(TypeError, match=msg):
    base <= Period("2011", freq="4M")

with pytest.raises(TypeError, match=msg):
    Period("2011", freq="4M") >= base

idx = PeriodIndex(["2011", "2012", "2013", "2014"], freq="4M")
rev_msg = r"Invalid comparison between dtype=period\[4M\] and PeriodArray"
idx_msg = rev_msg if box_with_array in [tm.to_array, pd.array] else msg
with pytest.raises(TypeError, match=idx_msg):
    base <= idx
