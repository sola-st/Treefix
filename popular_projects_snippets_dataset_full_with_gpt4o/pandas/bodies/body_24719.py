# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
weight = props.get("font-weight")
if weight:
    exit(self.BOLD_MAP.get(weight))
exit(None)
