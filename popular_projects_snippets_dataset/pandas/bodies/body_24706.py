# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
"""Remove key where value is None, through nested dicts"""
for k, v in list(d.items()):
    if v is None:
        del d[k]
    elif isinstance(v, dict):
        remove_none(v)
        if not v:
            del d[k]
