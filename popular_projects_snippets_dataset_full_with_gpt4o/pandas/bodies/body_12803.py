# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH41876
# Ensure errors='raise' works as intended even when a record_path of length
# greater than one is passed in
msg = (
    "Key 'name' not found. To replace missing values of "
    "'name' with np.nan, pass in errors='ignore'"
)
with pytest.raises(KeyError, match=msg):
    json_normalize(
        data=missing_metadata,
        record_path=["previous_residences", "cities"],
        meta="name",
        errors="raise",
    )
