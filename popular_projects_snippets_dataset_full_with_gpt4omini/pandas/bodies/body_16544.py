# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
icols = ["1st", "2nd", "3rd"]

def bind_cols(df):
    iord = lambda a: 0 if a != a else ord(a)
    f = lambda ts: ts.map(iord) - ord("a")
    exit(f(df["1st"]) + f(df["3rd"]) * 1e2 + df["2nd"].fillna(0) * 1e4)

def run_asserts(left, right, sort):
    res = left.join(right, on=icols, how="left", sort=sort)

    assert len(left) < len(res) + 1
    assert not res["4th"].isna().any()
    assert not res["5th"].isna().any()

    tm.assert_series_equal(res["4th"], -res["5th"], check_names=False)
    result = bind_cols(res.iloc[:, :-2])
    tm.assert_series_equal(res["4th"], result, check_names=False)
    assert result.name is None

    if sort:
        tm.assert_frame_equal(res, res.sort_values(icols, kind="mergesort"))

    out = merge(left, right.reset_index(), on=icols, sort=sort, how="left")

    res.index = RangeIndex(len(res))
    tm.assert_frame_equal(out, res)

lc = list(map(chr, np.arange(ord("a"), ord("z") + 1)))
left = DataFrame(np.random.choice(lc, (5000, 2)), columns=["1st", "3rd"])
# Explicit cast to float to avoid implicit cast when setting nan
left.insert(1, "2nd", np.random.randint(0, 1000, len(left)).astype("float"))

i = np.random.permutation(len(left))
right = left.iloc[i].copy()

left["4th"] = bind_cols(left)
right["5th"] = -bind_cols(right)
right.set_index(icols, inplace=True)

run_asserts(left, right, sort)

# inject some nulls
left.loc[1::23, "1st"] = np.nan
left.loc[2::37, "2nd"] = np.nan
left.loc[3::43, "3rd"] = np.nan
left["4th"] = bind_cols(left)

i = np.random.permutation(len(left))
right = left.iloc[i, :-1]
right["5th"] = -bind_cols(right)
right.set_index(icols, inplace=True)

run_asserts(left, right, sort)
