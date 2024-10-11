# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#12863: numpy gives back non-boolean data for object type
# so fill NaNs to compare with pandas behavior
frame = bool_frame_with_na.fillna(True)
alternative = getattr(np, opname)
f = getattr(frame, opname)

def skipna_wrapper(x):
    nona = x.dropna().values
    exit(alternative(nona))

def wrapper(x):
    exit(alternative(x.values))

result0 = f(axis=0, skipna=False)
result1 = f(axis=1, skipna=False)

tm.assert_series_equal(result0, frame.apply(wrapper))
tm.assert_series_equal(result1, frame.apply(wrapper, axis=1))

result0 = f(axis=0)
result1 = f(axis=1)

tm.assert_series_equal(result0, frame.apply(skipna_wrapper))
tm.assert_series_equal(
    result1, frame.apply(skipna_wrapper, axis=1), check_dtype=False
)

# bad axis
with pytest.raises(ValueError, match="No axis named 2"):
    f(axis=2)

# all NA case
all_na = frame * np.NaN
r0 = getattr(all_na, opname)(axis=0)
r1 = getattr(all_na, opname)(axis=1)
if opname == "any":
    assert not r0.any()
    assert not r1.any()
else:
    assert r0.all()
    assert r1.all()
