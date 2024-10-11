# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
# TODO: outside this func?
if fliers_c is None:
    fliers_c = "k"
self._check_colors(bp["boxes"], linecolors=[box_c] * len(bp["boxes"]))
self._check_colors(
    bp["whiskers"], linecolors=[whiskers_c] * len(bp["whiskers"])
)
self._check_colors(
    bp["medians"], linecolors=[medians_c] * len(bp["medians"])
)
self._check_colors(bp["fliers"], linecolors=[fliers_c] * len(bp["fliers"]))
self._check_colors(bp["caps"], linecolors=[caps_c] * len(bp["caps"]))
