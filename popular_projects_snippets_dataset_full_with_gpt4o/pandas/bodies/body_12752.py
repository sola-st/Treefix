# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
s = Series(
    [10, 20, 30, 40, 50, 60], name="series", index=[6, 7, 8, 9, 10, 15]
).sort_values()
nested = {"s1": s, "s2": s.copy()}
kwargs = {} if orient is None else {"orient": orient}

exp = {
    "s1": ujson.decode(ujson.encode(s, **kwargs)),
    "s2": ujson.decode(ujson.encode(s, **kwargs)),
}
assert ujson.decode(ujson.encode(nested, **kwargs)) == exp
