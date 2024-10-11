# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH#45648 - transform should align with the input's index
df = DataFrame({"a1": [1, 1, 3, 2, 2], "b": [5, 4, 3, 2, 1]})
if "a2" in keys:
    df["a2"] = df["a1"]
if keys_in_index:
    df = df.set_index(keys, append=True)

gb = df.groupby(keys)
if series:
    gb = gb["b"]

result = gb.transform(func)
expected = DataFrame({"b": expected_values}, index=df.index)
if series:
    expected = expected["b"]
tm.assert_equal(result, expected)
