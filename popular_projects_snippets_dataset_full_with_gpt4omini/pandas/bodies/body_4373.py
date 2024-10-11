# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/32289
a = DataFrame()
b = np.empty((0, 0))
with pytest.raises(ValueError, match=r"shape=\(1, 0, 0\)"):
    DataFrame([a])

with pytest.raises(ValueError, match=r"shape=\(1, 0, 0\)"):
    DataFrame([b])

a = DataFrame({"A": [1, 2]})
with pytest.raises(ValueError, match=r"shape=\(2, 2, 1\)"):
    DataFrame([a, a])
