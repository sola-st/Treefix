# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 12979
df = DataFrame(np.random.randn(5, 5))
self._check_bar_alignment(df, kind="bar", stacked=True, width=1)
self._check_bar_alignment(df, kind="barh", stacked=False, width=1)
self._check_bar_alignment(df, kind="barh", stacked=True, width=1)
self._check_bar_alignment(df, kind="bar", subplots=True, width=1)
self._check_bar_alignment(df, kind="barh", subplots=True, width=1)
