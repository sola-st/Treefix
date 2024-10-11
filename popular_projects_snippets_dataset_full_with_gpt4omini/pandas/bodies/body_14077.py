# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
n = 1000
s = Series(
    np.random.randint(-50, 50, n),
    index=[f"s{x:04d}" for x in range(n)],
    dtype="int64",
)

str_rep = str(s)
nmatches = len(re.findall("dtype", str_rep))
assert nmatches == 1
