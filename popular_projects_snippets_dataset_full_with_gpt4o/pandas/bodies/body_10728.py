# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# see gh-6620, gh-9311
df = DataFrame([{"a": 1, "b": i[0]}, {"a": 1, "b": i[1]}])

grp_exp = {
    "first": {"expected": i[0]},
    "last": {"expected": i[1]},
    "min": {"expected": i[0]},
    "max": {"expected": i[1]},
    "nth": {"expected": i[1], "args": [1]},
    "count": {"expected": 2},
}

for method, data in grp_exp.items():
    if "args" not in data:
        data["args"] = []

    grouped = df.groupby("a")
    res = getattr(grouped, method)(*data["args"])

    assert res.iloc[0].b == data["expected"]
