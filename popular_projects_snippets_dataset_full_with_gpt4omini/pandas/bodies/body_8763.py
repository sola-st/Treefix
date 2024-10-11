# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
arr = period_array(["2000", "2001"], freq="D")
with pytest.raises(IncompatibleFrequency, match="freq"):
    arr.take([0, -1], allow_fill=True, fill_value=pd.Period("2000", freq="W"))

msg = "value should be a 'Period' or 'NaT'. Got 'str' instead"
with pytest.raises(TypeError, match=msg):
    arr.take([0, -1], allow_fill=True, fill_value="foo")
