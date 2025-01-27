# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
for t in axis.get_majorticklabels():
    t.set_visible(False)

# set_visible will not be effective if
# minor axis has NullLocator and NullFormatter (default)
if isinstance(axis.get_minor_locator(), ticker.NullLocator):
    axis.set_minor_locator(ticker.AutoLocator())
if isinstance(axis.get_minor_formatter(), ticker.NullFormatter):
    axis.set_minor_formatter(ticker.FormatStrFormatter(""))
for t in axis.get_minorticklabels():
    t.set_visible(False)

axis.get_label().set_visible(False)
