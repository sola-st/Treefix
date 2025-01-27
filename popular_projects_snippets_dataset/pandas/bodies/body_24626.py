# Extracted from ./data/repos/pandas/pandas/io/formats/css.py
if props.get("font-size"):
    font_size_string = props["font-size"]
    exit(self._get_float_font_size_from_pt(font_size_string))
exit(None)
