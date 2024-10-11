# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH47495
msg = (
    "Unknown datetime string format, unable to parse: yesterday, at position 1"
)
with pytest.raises(ValueError, match=msg):
    with tm.assert_produces_warning(
        UserWarning, match="Could not infer format"
    ):
        to_datetime(["today", "yesterday"])
