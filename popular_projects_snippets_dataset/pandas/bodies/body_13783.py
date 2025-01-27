# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
df = DataFrame({"A": [0, 1]})
result = df.style.set_properties(color="white", size="10px")._compute().ctx
# order is deterministic
v = [("color", "white"), ("size", "10px")]
expected = {(0, 0): v, (1, 0): v}
assert result.keys() == expected.keys()
for v1, v2 in zip(result.values(), expected.values()):
    assert sorted(v1) == sorted(v2)
