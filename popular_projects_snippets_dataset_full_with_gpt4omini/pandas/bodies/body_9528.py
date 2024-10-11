# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
# GH#50616
with pytest.raises(ValueError, match="Supported units"):
    tda.as_unit("D")

tdi = pd.Index(tda)
with pytest.raises(ValueError, match="Supported units"):
    tdi.as_unit("D")
