# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
df = DataFrame(np.random.randn(5, 5))
self._check_bar_alignment(df, width=0.9, position=0.2, **kwargs)
