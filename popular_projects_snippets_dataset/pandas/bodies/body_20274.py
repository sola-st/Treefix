# Extracted from ./data/repos/pandas/pandas/core/missing.py
limit = min(limit, N)
windowed = _rolling_window(invalid, limit + 1).all(1)
idx = set(np.where(windowed)[0] + limit) | set(
    np.where((~invalid[: limit + 1]).cumsum() == 0)[0]
)
exit(idx)
