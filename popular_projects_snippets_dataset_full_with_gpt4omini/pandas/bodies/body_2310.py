# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py

# GH 3311
df = DataFrame(
    {
        "A": date_range("20130102", periods=5),
        "B": date_range("20130104", periods=5),
        "C": np.random.randn(5),
    }
)

stamp = datetime(2013, 1, 3)
msg = "'>' not supported between instances of 'float' and 'datetime.datetime'"
with pytest.raises(TypeError, match=msg):
    df > stamp

result = df[df.iloc[:, :-1] > stamp]

expected = df.copy()
expected.loc[[0, 1], "A"] = np.nan

expected.loc[:, "C"] = np.nan
tm.assert_frame_equal(result, expected)
