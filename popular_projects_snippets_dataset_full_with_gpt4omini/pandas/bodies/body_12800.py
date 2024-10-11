# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH14583:
# If meta keys are not always present a new option to set
# errors='ignore' has been implemented

msg = (
    "Key 'name' not found. To replace missing values of "
    "'name' with np.nan, pass in errors='ignore'"
)
with pytest.raises(KeyError, match=msg):
    json_normalize(
        data=missing_metadata,
        record_path="addresses",
        meta="name",
        errors="raise",
    )
