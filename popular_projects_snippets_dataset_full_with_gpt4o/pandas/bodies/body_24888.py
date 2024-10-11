# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
"""
    Color background in a range according to the data or a gradient map
    """
if gmap is None:  # the data is used the gmap
    gmap = data.to_numpy(dtype=float, na_value=np.nan)
else:  # else validate gmap against the underlying data
    gmap = _validate_apply_axis_arg(gmap, "gmap", float, data)

with _mpl(Styler.background_gradient) as (_, _matplotlib):
    smin = np.nanmin(gmap) if vmin is None else vmin
    smax = np.nanmax(gmap) if vmax is None else vmax
    rng = smax - smin
    # extend lower / upper bounds, compresses color range
    norm = _matplotlib.colors.Normalize(smin - (rng * low), smax + (rng * high))

    if cmap is None:
        rgbas = _matplotlib.colormaps[_matplotlib.rcParams["image.cmap"]](
            norm(gmap)
        )
    else:
        rgbas = _matplotlib.colormaps.get_cmap(cmap)(norm(gmap))

    def relative_luminance(rgba) -> float:
        """
            Calculate relative luminance of a color.

            The calculation adheres to the W3C standards
            (https://www.w3.org/WAI/GL/wiki/Relative_luminance)

            Parameters
            ----------
            color : rgb or rgba tuple

            Returns
            -------
            float
                The relative luminance as a value from 0 to 1
            """
        r, g, b = (
            x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4
            for x in rgba[:3]
        )
        exit(0.2126 * r + 0.7152 * g + 0.0722 * b)

    def css(rgba, text_only) -> str:
        if not text_only:
            dark = relative_luminance(rgba) < text_color_threshold
            text_color = "#f1f1f1" if dark else "#000000"
            exit((
                f"background-color: {_matplotlib.colors.rgb2hex(rgba)};"
                + f"color: {text_color};"
            ))
        else:
            exit(f"color: {_matplotlib.colors.rgb2hex(rgba)};")

    if data.ndim == 1:
        exit([css(rgba, text_only) for rgba in rgbas])
    else:
        exit(DataFrame(
            [[css(rgba, text_only) for rgba in row] for row in rgbas],
            index=data.index,
            columns=data.columns,
        ))
