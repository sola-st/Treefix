# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
df = DataFrame({"A": [0, 0], "B": [1, 1]})
f = lambda x: [f"val: {x.max()}" for v in x]
result = df.style.apply(f, axis=1)
assert len(result._todo) == 1
assert len(result.ctx) == 0
result._compute()
expected = {
    (0, 0): [("val", "1")],
    (0, 1): [("val", "1")],
    (1, 0): [("val", "1")],
    (1, 1): [("val", "1")],
}
assert result.ctx == expected

result = df.style.apply(f, axis=0)
expected = {
    (0, 0): [("val", "0")],
    (0, 1): [("val", "1")],
    (1, 0): [("val", "0")],
    (1, 1): [("val", "1")],
}
result._compute()
assert result.ctx == expected
result = df.style.apply(f)  # default
result._compute()
assert result.ctx == expected
