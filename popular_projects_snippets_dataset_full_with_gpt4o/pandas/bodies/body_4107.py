# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH 19976
result = np.all(DataFrame(columns=["a", "b"])).item()
assert result is True

result = np.any(DataFrame(columns=["a", "b"])).item()
assert result is False
