# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 13389
df1 = DataFrame({"entity_id": [101, 102]})
ser = Series([None, None], index=[101, 102], name="days")

dtype = f"datetime64[{unit}]"

if unit in ["D", "h", "m"]:
    # not supported so we cast to the nearest supported unit, seconds
    exp_dtype = "datetime64[s]"
else:
    exp_dtype = dtype
df2 = ser.astype(exp_dtype).to_frame("days")
assert df2["days"].dtype == exp_dtype

result = df1.merge(df2, left_on="entity_id", right_index=True)

days = np.array(["nat", "nat"], dtype=exp_dtype)
days = pd.core.arrays.DatetimeArray._simple_new(days, dtype=days.dtype)
exp = DataFrame(
    {
        "entity_id": [101, 102],
        "days": days,
    },
    columns=["entity_id", "days"],
)
assert exp["days"].dtype == exp_dtype
tm.assert_frame_equal(result, exp)
