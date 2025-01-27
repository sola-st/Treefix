# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# GH11619
idx = date_range("2015-01-01", "2015-12-31", freq="H", tz="Europe/Paris")
idx = idx._with_freq(None)  # freq does not round-trip
idx._data._freq = None  # otherwise there is trouble on unpickle
df = DataFrame({"values": 1, "idx": idx}, index=idx)
with tm.ensure_clean("csv_date_format_with_dst") as path:
    df.to_csv(path, index=True)
    result = read_csv(path, index_col=0)
    result.index = to_datetime(result.index, utc=True).tz_convert(
        "Europe/Paris"
    )
    result["idx"] = to_datetime(result["idx"], utc=True).astype(
        "datetime64[ns, Europe/Paris]"
    )
    tm.assert_frame_equal(result, df)

# assert working
df.astype(str)

with tm.ensure_clean("csv_date_format_with_dst") as path:
    df.to_pickle(path)
    result = pd.read_pickle(path)
    tm.assert_frame_equal(result, df)
