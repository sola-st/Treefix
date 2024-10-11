# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_dst.py
# .apply for non-Tick offsets throws AmbiguousTimeError when the target dt
# is dst-ambiguous
localized_dt = original_dt.tz_localize(tz)

msg = f"Cannot infer dst time from {target_dt}, try using the 'ambiguous' argument"
with pytest.raises(pytz.AmbiguousTimeError, match=msg):
    localized_dt + offset
