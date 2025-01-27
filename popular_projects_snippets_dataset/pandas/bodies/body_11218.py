# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_allowlist.py
df = df_letters
s = df_letters.floats

blocklist = [
    "eval",
    "query",
    "abs",
    "where",
    "mask",
    "align",
    "groupby",
    "clip",
    "astype",
    "at",
    "combine",
    "consolidate",
    "convert_objects",
]
to_methods = [method for method in dir(df) if method.startswith("to_")]

blocklist.extend(to_methods)

for bl in blocklist:
    for obj in (df, s):
        gb = obj.groupby(df.letters)

        # e.g., to_csv
        defined_but_not_allowed = (
            f"(?:^Cannot.+{repr(bl)}.+'{type(gb).__name__}'.+try "
            f"using the 'apply' method$)"
        )

        # e.g., query, eval
        not_defined = (
            f"(?:^'{type(gb).__name__}' object has no attribute {repr(bl)}$)"
        )

        msg = f"{defined_but_not_allowed}|{not_defined}"

        with pytest.raises(AttributeError, match=msg):
            getattr(gb, bl)
