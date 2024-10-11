# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
index = Index([1.5, 2, 3, 4, 5])
df = DataFrame(np.arange(5), index=index)

result = df.to_string()
expected = "     0\n1.5  0\n2.0  1\n3.0  2\n4.0  3\n5.0  4"
assert result == expected
