# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# Deprecation enforced from:
# https://github.com/pandas-dev/pandas/issues/31532
width = get_option("display.max_colwidth")
with pytest.raises(
    ValueError, match="Value must be a nonnegative integer or None"
):
    set_option("display.max_colwidth", -1)
set_option("display.max_colwidth", width)
