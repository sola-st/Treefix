# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
obj = frame_or_series(
    index=Index([True, False], dtype="boolean"), dtype="object"
)
obj.loc[bool_value]
