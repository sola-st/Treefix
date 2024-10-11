# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 10165
cols = MultiIndex.from_tuples(
    [
        ("syn", "A"),
        ("mis", "A"),
        ("non", "A"),
        ("syn", "C"),
        ("mis", "C"),
        ("non", "C"),
        ("syn", "T"),
        ("mis", "T"),
        ("non", "T"),
        ("syn", "G"),
        ("mis", "G"),
        ("non", "G"),
    ]
)
df = DataFrame(
    np.random.randint(1, 10, (4, 12)), columns=cols, index=["A", "C", "G", "T"]
)

msg = "transform must return a scalar value for each group.*"
with pytest.raises(ValueError, match=msg):
    df.groupby(axis=1, level=1).transform(lambda z: z.div(z.sum(axis=1), axis=0))
