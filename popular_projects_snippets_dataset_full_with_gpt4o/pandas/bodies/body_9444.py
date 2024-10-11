# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_cumulative.py
# GH#50297
arr = TimedeltaArray._from_sequence_not_strict(["1D", "2D"])
with pytest.raises(TypeError, match="cumprod not supported"):
    arr._accumulate("cumprod")
