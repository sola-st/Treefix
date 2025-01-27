# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/50255
with pytest.raises(
    ValueError, match="':' is a bad directive in format 'H%:M%:S%"
):
    to_datetime(["00:00:00"], format="H%:M%:S%", errors=errors)
