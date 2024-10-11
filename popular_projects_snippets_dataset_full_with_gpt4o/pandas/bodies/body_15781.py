# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# see GH#15524

if dtype not in (
    "S",
    "V",  # poor support (if any) currently
    "M",
    "m",  # Generic timestamps raise a ValueError. Already tested.
):
    init_empty = Series([], dtype=dtype)
    as_type_empty = Series([]).astype(dtype)
    tm.assert_series_equal(init_empty, as_type_empty)
