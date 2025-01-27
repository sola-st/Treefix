# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
try:
    datetime_series.fillna(method="ffil")
except ValueError as inst:
    assert "ffil" in str(inst)
