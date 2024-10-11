# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 12259
dates = [
    dt.datetime(1999, 12, 31, 12, 12, 12, 12000),
    dt.datetime(2012, 12, 21, 12, 21, 12, 21000),
    dt.datetime(1776, 7, 4, 7, 4, 7, 4000),
]
original = DataFrame(
    {
        "nums": [1.0, 2.0, 3.0],
        "strs": ["apple", "banana", "cherry"],
        "dates": dates,
    }
)

with tm.ensure_clean() as path:
    msg = "convert_dates key must be a column or an integer"
    with pytest.raises(ValueError, match=msg):
        original.to_stata(path, convert_dates={"wrong_name": "tc"})
