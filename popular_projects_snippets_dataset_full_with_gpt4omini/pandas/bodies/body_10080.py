# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py

c = frame_or_series(range(5)).ewm

# valid
c(com=0.5)
c(span=1.5)
c(alpha=0.5)
c(halflife=0.75)
c(com=0.5, span=None)
c(alpha=0.5, com=None)
c(halflife=0.75, alpha=None)

# not valid: mutually exclusive
msg = "comass, span, halflife, and alpha are mutually exclusive"
with pytest.raises(ValueError, match=msg):
    c(com=0.5, alpha=0.5)
with pytest.raises(ValueError, match=msg):
    c(span=1.5, halflife=0.75)
with pytest.raises(ValueError, match=msg):
    c(alpha=0.5, span=1.5)

# not valid: com < 0
msg = "comass must satisfy: comass >= 0"
with pytest.raises(ValueError, match=msg):
    c(com=-0.5)

# not valid: span < 1
msg = "span must satisfy: span >= 1"
with pytest.raises(ValueError, match=msg):
    c(span=0.5)

# not valid: halflife <= 0
msg = "halflife must satisfy: halflife > 0"
with pytest.raises(ValueError, match=msg):
    c(halflife=0)

# not valid: alpha <= 0 or alpha > 1
msg = "alpha must satisfy: 0 < alpha <= 1"
for alpha in (-0.5, 1.5):
    with pytest.raises(ValueError, match=msg):
        c(alpha=alpha)
