# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
A = series.ewm(com=13.932726172912965).mean()
B = series.ewm(halflife=10.0).mean()
tm.assert_almost_equal(A, B)
msg = "comass, span, halflife, and alpha are mutually exclusive"
with pytest.raises(ValueError, match=msg):
    series.ewm(span=20, halflife=50)
with pytest.raises(ValueError, match=msg):
    series.ewm(com=9.5, halflife=50)
with pytest.raises(ValueError, match=msg):
    series.ewm(com=9.5, span=20, halflife=50)
msg = "Must pass one of comass, span, halflife, or alpha"
with pytest.raises(ValueError, match=msg):
    series.ewm()
