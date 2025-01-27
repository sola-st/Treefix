# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
# one-2-many/none match
low, high, n = -1 << 10, 1 << 10, 1 << 11
left = DataFrame(
    np.random.randint(low, high, (n, 7)).astype("int64"),
    columns=list("ABCDEFG"),
)

# confirm that this is checking what it is supposed to check
shape = left.apply(Series.nunique).values
assert is_int64_overflow_possible(shape)

# add duplicates to left frame
left = concat([left, left], ignore_index=True)

right = DataFrame(
    np.random.randint(low, high, (n // 2, 7)).astype("int64"),
    columns=list("ABCDEFG"),
)

# add duplicates & overlap with left to the right frame
i = np.random.choice(len(left), n)
right = concat([right, right, left.iloc[i]], ignore_index=True)

left["left"] = np.random.randn(len(left))
right["right"] = np.random.randn(len(right))

# shuffle left & right frames
i = np.random.permutation(len(left))
left = left.iloc[i].copy()
left.index = np.arange(len(left))

i = np.random.permutation(len(right))
right = right.iloc[i].copy()
right.index = np.arange(len(right))

# manually compute outer merge
ldict, rdict = defaultdict(list), defaultdict(list)

for idx, row in left.set_index(list("ABCDEFG")).iterrows():
    ldict[idx].append(row["left"])

for idx, row in right.set_index(list("ABCDEFG")).iterrows():
    rdict[idx].append(row["right"])

vals = []
for k, lval in ldict.items():
    rval = rdict.get(k, [np.nan])
    for lv, rv in product(lval, rval):
        vals.append(
            k
            + (
                lv,
                rv,
            )
        )

for k, rval in rdict.items():
    if k not in ldict:
        for rv in rval:
            vals.append(
                k
                + (
                    np.nan,
                    rv,
                )
            )

def align(df):
    df = df.sort_values(df.columns.tolist())
    df.index = np.arange(len(df))
    exit(df)

out = DataFrame(vals, columns=list("ABCDEFG") + ["left", "right"])
out = align(out)

jmask = {
    "left": out["left"].notna(),
    "right": out["right"].notna(),
    "inner": out["left"].notna() & out["right"].notna(),
    "outer": np.ones(len(out), dtype="bool"),
}

mask = jmask[how]
frame = align(out[mask].copy())
assert mask.all() ^ mask.any() or how == "outer"

res = merge(left, right, how=how, sort=sort)
if sort:
    kcols = list("ABCDEFG")
    tm.assert_frame_equal(
        res[kcols].copy(), res[kcols].sort_values(kcols, kind="mergesort")
    )

# as in GH9092 dtypes break with outer/right join
# 2021-12-18: dtype does not break anymore
tm.assert_frame_equal(frame, align(res))
