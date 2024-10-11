# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame({"a": np.arange(100)}, index=np.arange(100))

ax = df.plot(logy=input_log)
self._check_ax_scales(ax, yaxis=expected_log)
assert ax.get_yscale() == expected_log

ax = df.plot(logx=input_log)
self._check_ax_scales(ax, xaxis=expected_log)
assert ax.get_xscale() == expected_log

ax = df.plot(loglog=input_log)
self._check_ax_scales(ax, xaxis=expected_log, yaxis=expected_log)
assert ax.get_xscale() == expected_log
assert ax.get_yscale() == expected_log
