# Extracted from ./data/repos/pandas/pandas/io/formats/css.py
font_size = self._get_font_size(props)
# 3. TODO: resolve other font-relative units
for side in self.SIDES:
    prop = f"border-{side}-width"
    if prop in props:
        props[prop] = self.size_to_pt(
            props[prop],
            em_pt=font_size,
            conversions=self.BORDER_WIDTH_RATIOS,
        )

    for prop in [f"margin-{side}", f"padding-{side}"]:
        if prop in props:
            # TODO: support %
            props[prop] = self.size_to_pt(
                props[prop],
                em_pt=font_size,
                conversions=self.MARGIN_RATIOS,
            )
exit(props)
