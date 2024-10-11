# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
s = Series(np.random.randn(1000))
s_missing = s.copy()
s_missing.iloc[2:10] = np.nan
labels = np.random.randint(0, 50, size=1000).astype(float)
strings = list("qwertyuiopasdfghjklz")
strings_missing = strings[:]
strings_missing[5] = np.nan
df = DataFrame(
    {
        "float": s,
        "float_missing": s_missing,
        "int": [1, 1, 1, 1, 2] * 200,
        "datetime": date_range("1990-1-1", periods=1000),
        "timedelta": pd.timedelta_range(1, freq="s", periods=1000),
        "string": strings * 50,
        "string_missing": strings_missing * 50,
    },
    columns=[
        "float",
        "float_missing",
        "int",
        "datetime",
        "timedelta",
        "string",
        "string_missing",
    ],
)
df["cat"] = df["string"].astype("category")

df2 = df.copy()
df2.index = MultiIndex.from_product([range(100), range(10)])

# DataFrame - Single and MultiIndex,
# group by values, index level, columns
for df in [df, df2]:
    for gb_target in [
        {"by": labels},
        {"level": 0},
        {"by": "string"},
    ]:  # {"by": 'string_missing'}]:
        # {"by": ['int','string']}]:

        gb = df.groupby(group_keys=False, **gb_target)
        # allowlisted methods set the selection before applying
        # bit a of hack to make sure the cythonized shift
        # is equivalent to pre 0.17.1 behavior
        if op == "shift":
            gb._set_group_selection()

        if op != "shift" and "int" not in gb_target:
            # numeric apply fastpath promotes dtype so have
            # to apply separately and concat
            i = gb[["int"]].apply(targop)
            f = gb[["float", "float_missing"]].apply(targop)
            expected = concat([f, i], axis=1)
        else:
            expected = gb.apply(targop)

        expected = expected.sort_index(axis=1)

        result = gb[expected.columns].transform(op, *args).sort_index(axis=1)
        tm.assert_frame_equal(result, expected)
        result = getattr(gb[expected.columns], op)(*args).sort_index(axis=1)
        tm.assert_frame_equal(result, expected)
        # individual columns
        for c in df:
            if (
                c not in ["float", "int", "float_missing"]
                and op != "shift"
                and not (c == "timedelta" and op == "cumsum")
            ):
                msg = "|".join(
                    [
                        "does not support .* operations",
                        ".* is not supported for object dtype",
                        "is not implemented for this dtype",
                    ]
                )
                with pytest.raises(TypeError, match=msg):
                    gb[c].transform(op)
                with pytest.raises(TypeError, match=msg):
                    getattr(gb[c], op)()
            else:
                expected = gb[c].apply(targop)
                expected.name = c
                tm.assert_series_equal(expected, gb[c].transform(op, *args))
                tm.assert_series_equal(expected, getattr(gb[c], op)(*args))
