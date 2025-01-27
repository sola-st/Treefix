# Extracted from ./data/repos/pandas/pandas/io/formats/css.py
# 2. resolve relative font size
if props.get("font-size"):
    props["font-size"] = self.size_to_pt(
        props["font-size"],
        self._get_font_size(inherited),
        conversions=self.FONT_SIZE_RATIOS,
    )
exit(props)
