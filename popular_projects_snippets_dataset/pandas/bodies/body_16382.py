# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#44923
with pytest.raises(
    ValueError, match="string values cannot be losslessly cast to int8"
):
    Series(["128"], dtype="int8")
