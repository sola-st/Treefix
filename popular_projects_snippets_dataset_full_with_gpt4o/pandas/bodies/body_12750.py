# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
df = DataFrame(
    [[1, 2, 3], [4, 5, 6]], index=["a", "b"], columns=["x", "y", "z"]
)

nested = {"df1": df, "df2": df.copy()}
kwargs = {} if orient is None else {"orient": orient}

exp = {
    "df1": ujson.decode(ujson.encode(df, **kwargs)),
    "df2": ujson.decode(ujson.encode(df, **kwargs)),
}
assert ujson.decode(ujson.encode(nested, **kwargs)) == exp
