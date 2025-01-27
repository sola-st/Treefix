# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# CASE 2: invalid input
# cannot consistently process with single format
# ValueError *always* raised

# first in DD/MM/YYYY, second in MM/DD/YYYY
arr = ["31/12/2014", "03/30/2011"]

with pytest.raises(
    ValueError,
    match=(
        r'^time data "03/30/2011" doesn\'t match format '
        r'"%d/%m/%Y", at position 1$'
    ),
):
    to_datetime(arr, dayfirst=True)
