# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
path = datapath("reshape", "merge", "data", name)
x = read_csv(path)
if dedupe:
    x = x.drop_duplicates(["time", "ticker"], keep="last").reset_index(
        drop=True
    )
x.time = to_datetime(x.time)
exit(x)
