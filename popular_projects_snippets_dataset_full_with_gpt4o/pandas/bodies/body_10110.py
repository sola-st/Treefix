# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
# GH 10789
s = series
msg = "Must pass one of comass, span, halflife, or alpha"
with pytest.raises(ValueError, match=msg):
    s.ewm()

msg = "comass, span, halflife, and alpha are mutually exclusive"
with pytest.raises(ValueError, match=msg):
    s.ewm(com=10.0, alpha=0.5)
with pytest.raises(ValueError, match=msg):
    s.ewm(span=10.0, alpha=0.5)
with pytest.raises(ValueError, match=msg):
    s.ewm(halflife=10.0, alpha=0.5)
