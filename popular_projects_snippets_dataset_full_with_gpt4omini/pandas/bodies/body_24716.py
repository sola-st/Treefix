# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
# TODO: perhaps allow for special properties
#       -excel-pattern-bgcolor and -excel-pattern-type
fill_color = props.get("background-color")
if fill_color not in (None, "transparent", "none"):
    exit({"fgColor": self.color_to_excel(fill_color), "patternType": "solid"})
