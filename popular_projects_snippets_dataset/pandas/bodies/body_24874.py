# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
if subset is None and gmap is None:
    subset = self._get_numeric_subset_default()

exit(self.apply(
    _background_gradient,
    cmap=cmap,
    subset=subset,
    axis=axis,
    low=low,
    high=high,
    vmin=vmin,
    vmax=vmax,
    gmap=gmap,
    text_only=True,
))
