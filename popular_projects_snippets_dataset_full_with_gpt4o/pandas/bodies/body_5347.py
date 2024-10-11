# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
initial = Period("2013")

assert initial.asfreq(freq="M", how="S") == Period("2013-01", "M")

msg = INVALID_FREQ_ERR_MSG
with pytest.raises(ValueError, match=msg):
    initial.asfreq(freq="MS", how="S")

with pytest.raises(ValueError, match=msg):
    Period("2013-01", "MS")

assert _period_code_map.get("MS") is None
