# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# GH46210
with pytest.raises(
    ValueError,
    match=(
        r'^time data "31/05/2000" doesn\'t match format "%m/%d/%Y", at position 1$'
    ),
):
    pd.to_datetime(["01/01/2000", "31/05/2000", "31/05/2001", "01/02/2000"])
