# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
font_style = props.get("font-style")
if font_style:
    exit(self.ITALIC_MAP.get(font_style))
exit(None)
