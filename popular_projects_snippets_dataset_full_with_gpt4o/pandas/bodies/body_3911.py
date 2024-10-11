# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH9497 - multiple unstack with nulls
from l3.Runtime import _l_
df = DataFrame(
    {
        "1st": [1, 2, 1, 2, 1, 2],
        "2nd": date_range("2014-02-01", periods=6, freq="D"),
        "jim": 100 + np.arange(6),
        "joe": (np.random.randn(6) * 10).round(2),
    }
)
_l_(20973)

df["3rd"] = df["2nd"] - pd.Timestamp("2014-02-02")
_l_(20974)
df.loc[1, "2nd"] = df.loc[3, "2nd"] = np.nan
_l_(20975)
df.loc[1, "3rd"] = df.loc[4, "3rd"] = np.nan
_l_(20976)

left = df.set_index(["1st", "2nd", "3rd"]).unstack(["2nd", "3rd"])
_l_(20977)
assert left.notna().values.sum() == 2 * len(df)
_l_(20978)

for col in ["jim", "joe"]:
    _l_(20982)

    for _, r in df.iterrows():
        _l_(20981)

        key = r["1st"], (col, r["2nd"], r["3rd"])
        _l_(20979)
        assert r[col] == left.loc[key]
        _l_(20980)
