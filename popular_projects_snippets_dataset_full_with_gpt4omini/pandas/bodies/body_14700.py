# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH2157
df = DataFrame({"A": [3] * 5, "B": list(range(5))}, index=range(5))
self._check_bar_alignment(df, **kwargs)
