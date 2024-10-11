# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH 19603
index = DatetimeIndex(
    ["2018-02-08 15:00:00.168456358", "2018-02-08 15:00:00.168456359"], tz=tz
)
for i, ts in enumerate(index):
    assert ts == index[i]  # pylint: disable=unnecessary-list-index-lookup
