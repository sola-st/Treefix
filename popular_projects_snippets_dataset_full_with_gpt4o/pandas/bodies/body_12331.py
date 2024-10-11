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
    original.to_stata(path, write_index=False)
    reread = read_stata(path, convert_dates=True)
    tm.assert_frame_equal(original, reread)

    original.to_stata(path, write_index=False, convert_dates={"dates": "tc"})
    direct = read_stata(path, convert_dates=True)
    tm.assert_frame_equal(reread, direct)

    dates_idx = original.columns.tolist().index("dates")
    original.to_stata(path, write_index=False, convert_dates={dates_idx: "tc"})
    direct = read_stata(path, convert_dates=True)
    tm.assert_frame_equal(reread, direct)
