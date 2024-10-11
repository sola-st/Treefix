# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
df = DataFrame([[1, np.nan], [1, 4], [5, 6]], columns=["A", "B"])
g = df.groupby("A")

tm.assert_frame_equal(g.nth(0), df.iloc[[0, 2]])
tm.assert_frame_equal(g.nth(1), df.iloc[[1]])
tm.assert_frame_equal(g.nth(2), df.loc[[]])
tm.assert_frame_equal(g.nth(-1), df.iloc[[1, 2]])
tm.assert_frame_equal(g.nth(-2), df.iloc[[0]])
tm.assert_frame_equal(g.nth(-3), df.loc[[]])
tm.assert_series_equal(g.B.nth(0), df.B.iloc[[0, 2]])
tm.assert_series_equal(g.B.nth(1), df.B.iloc[[1]])
tm.assert_frame_equal(g[["B"]].nth(0), df[["B"]].iloc[[0, 2]])

tm.assert_frame_equal(g.nth(0, dropna="any"), df.iloc[[1, 2]])
tm.assert_frame_equal(g.nth(-1, dropna="any"), df.iloc[[1, 2]])

tm.assert_frame_equal(g.nth(7, dropna="any"), df.iloc[:0])
tm.assert_frame_equal(g.nth(2, dropna="any"), df.iloc[:0])

# out of bounds, regression from 0.13.1
# GH 6621
df = DataFrame(
    {
        "color": {0: "green", 1: "green", 2: "red", 3: "red", 4: "red"},
        "food": {0: "ham", 1: "eggs", 2: "eggs", 3: "ham", 4: "pork"},
        "two": {
            0: 1.5456590000000001,
            1: -0.070345000000000005,
            2: -2.4004539999999999,
            3: 0.46206000000000003,
            4: 0.52350799999999997,
        },
        "one": {
            0: 0.56573799999999996,
            1: -0.9742360000000001,
            2: 1.033801,
            3: -0.78543499999999999,
            4: 0.70422799999999997,
        },
    }
).set_index(["color", "food"])

result = df.groupby(level=0, as_index=False).nth(2)
expected = df.iloc[[-1]]
tm.assert_frame_equal(result, expected)

result = df.groupby(level=0, as_index=False).nth(3)
expected = df.loc[[]]
tm.assert_frame_equal(result, expected)

# GH 7559
# from the vbench
df = DataFrame(np.random.randint(1, 10, (100, 2)), dtype="int64")
s = df[1]
g = df[0]
expected = s.groupby(g).first()
expected2 = s.groupby(g).apply(lambda x: x.iloc[0])
tm.assert_series_equal(expected2, expected, check_names=False)
assert expected.name == 1
assert expected2.name == 1

# validate first
v = s[g == 1].iloc[0]
assert expected.iloc[0] == v
assert expected2.iloc[0] == v

with pytest.raises(ValueError, match="For a DataFrame"):
    s.groupby(g, sort=False).nth(0, dropna=True)

# doc example
df = DataFrame([[1, np.nan], [1, 4], [5, 6]], columns=["A", "B"])
g = df.groupby("A")
result = g.B.nth(0, dropna="all")
expected = df.B.iloc[[1, 2]]
tm.assert_series_equal(result, expected)

# test multiple nth values
df = DataFrame([[1, np.nan], [1, 3], [1, 4], [5, 6], [5, 7]], columns=["A", "B"])
g = df.groupby("A")

tm.assert_frame_equal(g.nth(0), df.iloc[[0, 3]])
tm.assert_frame_equal(g.nth([0]), df.iloc[[0, 3]])
tm.assert_frame_equal(g.nth([0, 1]), df.iloc[[0, 1, 3, 4]])
tm.assert_frame_equal(g.nth([0, -1]), df.iloc[[0, 2, 3, 4]])
tm.assert_frame_equal(g.nth([0, 1, 2]), df.iloc[[0, 1, 2, 3, 4]])
tm.assert_frame_equal(g.nth([0, 1, -1]), df.iloc[[0, 1, 2, 3, 4]])
tm.assert_frame_equal(g.nth([2]), df.iloc[[2]])
tm.assert_frame_equal(g.nth([3, 4]), df.loc[[]])

business_dates = pd.date_range(start="4/1/2014", end="6/30/2014", freq="B")
df = DataFrame(1, index=business_dates, columns=["a", "b"])
# get the first, fourth and last two business days for each month
key = [df.index.year, df.index.month]
result = df.groupby(key, as_index=False).nth([0, 3, -2, -1])
expected_dates = pd.to_datetime(
    [
        "2014/4/1",
        "2014/4/4",
        "2014/4/29",
        "2014/4/30",
        "2014/5/1",
        "2014/5/6",
        "2014/5/29",
        "2014/5/30",
        "2014/6/2",
        "2014/6/5",
        "2014/6/27",
        "2014/6/30",
    ]
)
expected = DataFrame(1, columns=["a", "b"], index=expected_dates)
tm.assert_frame_equal(result, expected)
