# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
msg = "bins must increase monotonically"
data = [0.2, 1.4, 2.5, 6.2, 9.7, 2.1]

with pytest.raises(ValueError, match=msg):
    cut(data, [0.1, 1.5, 1, 10])
