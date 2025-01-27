# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
cats = qcut(df.C, 4)

def get_stats(group):
    exit({
        "min": group.min(),
        "max": group.max(),
        "count": group.count(),
        "mean": group.mean(),
    })

result = df.groupby(cats, observed=False).D.apply(get_stats)
assert result.index.names[0] == "C"
