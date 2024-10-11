# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
# GH 13500
index = date_range(datetime(2005, 1, 1), datetime(2005, 1, 10), freq="D")

rng = np.arange(len(index), dtype=np.int64)
df = DataFrame(
    {"date": index, "a": rng},
    index=pd.MultiIndex.from_arrays([rng, index], names=["v", "d"]),
)
df_exp = DataFrame({"a": rng}, index=index)

# non DatetimeIndex
msg = (
    "Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, "
    "but got an instance of 'NumericIndex'"
)
with pytest.raises(TypeError, match=msg):
    df.resample("2D", level="v")

msg = "The Grouper cannot specify both a key and a level!"
with pytest.raises(ValueError, match=msg):
    df.resample("2D", on="date", level="d")

msg = "unhashable type: 'list'"
with pytest.raises(TypeError, match=msg):
    df.resample("2D", on=["a", "date"])

msg = r"\"Level \['a', 'date'\] not found\""
with pytest.raises(KeyError, match=msg):
    df.resample("2D", level=["a", "date"])

# upsampling not allowed
msg = (
    "Upsampling from level= or on= selection is not supported, use "
    r"\.set_index\(\.\.\.\) to explicitly set index to datetime-like"
)
with pytest.raises(ValueError, match=msg):
    df.resample("2D", level="d").asfreq()
with pytest.raises(ValueError, match=msg):
    df.resample("2D", on="date").asfreq()

exp = df_exp.resample("2D").sum()
exp.index.name = "date"
result = df.resample("2D", on="date").sum()
tm.assert_frame_equal(exp, result)

exp.index.name = "d"
with pytest.raises(TypeError, match="datetime64 type does not support sum"):
    df.resample("2D", level="d").sum()
result = df.resample("2D", level="d").sum(numeric_only=True)
tm.assert_frame_equal(exp, result)
