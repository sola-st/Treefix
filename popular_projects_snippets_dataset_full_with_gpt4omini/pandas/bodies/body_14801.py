# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
lines = []
errs = [c.lines for c in ax.containers if getattr(c, has_err, False)][0]
for el in errs:
    if is_list_like(el):
        lines.extend(el)
    else:
        lines.append(el)
err_lines = [x for x in lines if x in ax.collections]
self._check_colors(
    err_lines, linecolors=np.array([expected] * len(err_lines))
)
