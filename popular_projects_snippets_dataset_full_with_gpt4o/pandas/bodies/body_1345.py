# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py

# GH 3631, iloc with a mask (of a series) should raise
df = DataFrame(list(range(5)), index=list("ABCDE"), columns=["a"])
mask = df.a % 2 == 0
msg = "iLocation based boolean indexing cannot use an indexable as a mask"
with pytest.raises(ValueError, match=msg):
    df.iloc[mask]
mask.index = range(len(mask))
msg = "iLocation based boolean indexing on an integer type is not available"
with pytest.raises(NotImplementedError, match=msg):
    df.iloc[mask]

# ndarray ok
result = df.iloc[np.array([True] * len(mask), dtype=bool)]
tm.assert_frame_equal(result, df)

# the possibilities
locs = np.arange(4)
nums = 2**locs
reps = [bin(num) for num in nums]
df = DataFrame({"locs": locs, "nums": nums}, reps)

expected = {
    (None, ""): "0b1100",
    (None, ".loc"): "0b1100",
    (None, ".iloc"): "0b1100",
    ("index", ""): "0b11",
    ("index", ".loc"): "0b11",
    ("index", ".iloc"): (
        "iLocation based boolean indexing cannot use an indexable as a mask"
    ),
    ("locs", ""): "Unalignable boolean Series provided as indexer "
    "(index of the boolean Series and of the indexed "
    "object do not match).",
    ("locs", ".loc"): "Unalignable boolean Series provided as indexer "
    "(index of the boolean Series and of the "
    "indexed object do not match).",
    ("locs", ".iloc"): (
        "iLocation based boolean indexing on an "
        "integer type is not available"
    ),
}

# UserWarnings from reindex of a boolean mask
with catch_warnings(record=True):
    simplefilter("ignore", UserWarning)
    for idx in [None, "index", "locs"]:
        mask = (df.nums > 2).values
        if idx:
            mask = Series(mask, list(reversed(getattr(df, idx))))
        for method in ["", ".loc", ".iloc"]:
            try:
                if method:
                    accessor = getattr(df, method[1:])
                else:
                    accessor = df
                answer = str(bin(accessor[mask]["nums"].sum()))
            except (ValueError, IndexingError, NotImplementedError) as e:
                answer = str(e)

            key = (
                idx,
                method,
            )
            r = expected.get(key)
            if r != answer:
                raise AssertionError(
                    f"[{key}] does not match [{answer}], received [{r}]"
                )
