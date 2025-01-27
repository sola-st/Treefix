# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

# tz, 8260
with tm.ensure_clean("__tmp_to_csv_from_csv5__") as path:

    timezone_frame.to_csv(path)
    result = read_csv(path, index_col=0, parse_dates=["A"])

    converter = (
        lambda c: to_datetime(result[c])
        .dt.tz_convert("UTC")
        .dt.tz_convert(timezone_frame[c].dt.tz)
    )
    result["B"] = converter("B")
    result["C"] = converter("C")
    tm.assert_frame_equal(result, timezone_frame)
