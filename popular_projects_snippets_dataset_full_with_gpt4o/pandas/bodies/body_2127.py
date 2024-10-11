# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 48633
ts_strings = ["200622-12-31", "111111-24-11"]
msg = (
    'Parsed string "200622-12-31" gives an invalid tzoffset, which must '
    r"be between -timedelta\(hours=24\) and timedelta\(hours=24\), "
    "at position 0"
)
with pytest.raises(
    ValueError,
    match=msg,
):
    with tm.assert_produces_warning(
        UserWarning, match="Could not infer format"
    ):
        to_datetime(
            ts_strings,
            errors="raise",
        )
