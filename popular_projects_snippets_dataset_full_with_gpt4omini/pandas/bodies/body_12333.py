# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
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

msg = "Format %tC not implemented"
with pytest.raises(NotImplementedError, match=msg):
    with tm.ensure_clean() as path:
        original.to_stata(path, convert_dates={"dates": "tC"})

dates = pd.date_range("1-1-1990", periods=3, tz="Asia/Hong_Kong")
original = DataFrame(
    {
        "nums": [1.0, 2.0, 3.0],
        "strs": ["apple", "banana", "cherry"],
        "dates": dates,
    }
)
with pytest.raises(NotImplementedError, match="Data type datetime64"):
    with tm.ensure_clean() as path:
        original.to_stata(path)
