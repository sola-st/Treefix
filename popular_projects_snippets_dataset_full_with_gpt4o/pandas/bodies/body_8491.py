# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
# GH 24076
idx = date_range(
    start="2018-12-02 14:50:00-07:00",
    end="2018-12-02 14:50:00-07:00",
    freq="1min",
)
df = DataFrame(1, index=idx, columns=["A"])
result = df[start:end]
expected = df.iloc[0:3, :]
tm.assert_frame_equal(result, expected)

# GH 16785
start = str(start)
end = str(end)
with pytest.raises(ValueError, match="Both dates must"):
    df[start : end[:-4] + "1:00"]

with pytest.raises(ValueError, match="The index must be timezone"):
    df = df.tz_localize(None)
    df[start:end]
