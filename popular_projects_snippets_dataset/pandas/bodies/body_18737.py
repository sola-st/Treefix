# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    MultiIndex with a level that is a tzaware DatetimeIndex.
    """
# GH#8367 round trip with pickle
exit(MultiIndex.from_product(
    [[1, 2], ["a", "b"], pd.date_range("20130101", periods=3, tz="US/Eastern")],
    names=["one", "two", "three"],
))
