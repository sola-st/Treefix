# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
if props.get("white-space") is None:
    exit(None)
exit(bool(props["white-space"] not in ("nowrap", "pre", "pre-line")))
