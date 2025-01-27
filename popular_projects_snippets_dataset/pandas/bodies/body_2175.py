# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/12649
with pytest.raises(
    ValueError,
    match=(
        rf"time data \"{input}\" doesn\'t match format "
        rf"\"{format}\", at position 0"
    ),
):
    to_datetime(input, format=format)
