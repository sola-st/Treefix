# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 5267
# be datelike friendly
df = DataFrame(
    {
        "DATE": pd.to_datetime(
            [
                "10-Oct-2013",
                "10-Oct-2013",
                "10-Oct-2013",
                "11-Oct-2013",
                "11-Oct-2013",
                "11-Oct-2013",
            ]
        ),
        "label": ["foo", "foo", "bar", "foo", "foo", "bar"],
        "VAL": [1, 2, 3, 4, 5, 6],
    }
)

g = df.groupby("DATE")
key = list(g.groups)[0]
result1 = g.get_group(key)
result2 = g.get_group(Timestamp(key).to_pydatetime())
result3 = g.get_group(str(Timestamp(key)))
tm.assert_frame_equal(result1, result2)
tm.assert_frame_equal(result1, result3)

g = df.groupby(["DATE", "label"])

key = list(g.groups)[0]
result1 = g.get_group(key)
result2 = g.get_group((Timestamp(key[0]).to_pydatetime(), key[1]))
result3 = g.get_group((str(Timestamp(key[0])), key[1]))
tm.assert_frame_equal(result1, result2)
tm.assert_frame_equal(result1, result3)

# must pass a same-length tuple with multiple keys
msg = "must supply a tuple to get_group with multiple grouping keys"
with pytest.raises(ValueError, match=msg):
    g.get_group("foo")
with pytest.raises(ValueError, match=msg):
    g.get_group("foo")
msg = "must supply a same-length tuple to get_group with multiple grouping keys"
with pytest.raises(ValueError, match=msg):
    g.get_group(("foo", "bar", "baz"))
