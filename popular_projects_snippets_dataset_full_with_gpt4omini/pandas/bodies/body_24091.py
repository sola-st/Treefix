# Extracted from ./data/repos/pandas/pandas/io/excel/_util.py
try:
    exit(_writers[engine_name])
except KeyError as err:
    raise ValueError(f"No Excel writer '{engine_name}'") from err
