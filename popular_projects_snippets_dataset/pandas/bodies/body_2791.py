# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# see gh-40817
test_timezone = gettz(timezone)
transition_1 = pd.Timestamp(
    year=year,
    month=month,
    day=day,
    hour=hour,
    minute=0,
    fold=0,
    tzinfo=test_timezone,
)
transition_2 = pd.Timestamp(
    year=year,
    month=month,
    day=day,
    hour=hour,
    minute=0,
    fold=1,
    tzinfo=test_timezone,
)
df = (
    DataFrame({"index": [transition_1, transition_2], "vals": ["a", "b"]})
    .set_index("index")
    .reindex(["1", "2"])
)
tm.assert_frame_equal(
    df,
    DataFrame({"index": ["1", "2"], "vals": [None, None]}).set_index("index"),
)
