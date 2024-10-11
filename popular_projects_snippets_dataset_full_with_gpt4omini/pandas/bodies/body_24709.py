# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
vertical_align = props.get("vertical-align")
if vertical_align:
    exit(self.VERTICAL_MAP.get(vertical_align))
exit(None)
