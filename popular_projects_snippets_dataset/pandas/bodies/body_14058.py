# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame(np.random.random(size=(3, 3)), columns=["a", "b", "c"])

result = df.to_string(col_space={"a": 10, "b": 11, "c": 12})
# 3 separating space + each col_space for (id, a, b, c)
assert len(result.split("\n")[1]) == (3 + 1 + 10 + 11 + 12)

result = df.to_string(col_space=[10, 11, 12])
assert len(result.split("\n")[1]) == (3 + 1 + 10 + 11 + 12)
