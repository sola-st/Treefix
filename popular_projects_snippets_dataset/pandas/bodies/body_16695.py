# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 13389
df1 = DataFrame({"entity_id": [101, 102]})
ser = Series([None, None], index=[101, 102], name="days")

dtype = f"m8[{unit}]"
if unit in ["D", "h", "m"]:
    # We cannot astype, instead do nearest supported unit, i.e. "s"
    msg = "Supported resolutions are 's', 'ms', 'us', 'ns'"
    with pytest.raises(ValueError, match=msg):
        ser.astype(dtype)

    df2 = ser.astype("m8[s]").to_frame("days")
else:
    df2 = ser.astype(dtype).to_frame("days")
    assert df2["days"].dtype == dtype

result = df1.merge(df2, left_on="entity_id", right_index=True)

exp = DataFrame(
    {"entity_id": [101, 102], "days": np.array(["nat", "nat"], dtype=dtype)},
    columns=["entity_id", "days"],
)
tm.assert_frame_equal(result, exp)
