# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py

# big mixed
biggie = DataFrame(
    {"A": np.random.randn(200), "B": tm.makeStringIndex(200)},
)

biggie.loc[:20, "A"] = np.nan
biggie.loc[:20, "B"] = np.nan
s = biggie.to_string()

buf = StringIO()
retval = biggie.to_string(buf=buf)
assert retval is None
assert buf.getvalue() == s

assert isinstance(s, str)

# print in right order
result = biggie.to_string(
    columns=["B", "A"], col_space=17, float_format="%.5f".__mod__
)
lines = result.split("\n")
header = lines[0].strip().split()
joined = "\n".join([re.sub(r"\s+", " ", x).strip() for x in lines[1:]])
recons = read_csv(StringIO(joined), names=header, header=None, sep=" ")
tm.assert_series_equal(recons["B"], biggie["B"])
assert recons["A"].count() == biggie["A"].count()
assert (np.abs(recons["A"].dropna() - biggie["A"].dropna()) < 0.1).all()

# expected = ['B', 'A']
# assert header == expected

result = biggie.to_string(columns=["A"], col_space=17)
header = result.split("\n")[0].strip().split()
expected = ["A"]
assert header == expected

biggie.to_string(columns=["B", "A"], formatters={"A": lambda x: f"{x:.1f}"})

biggie.to_string(columns=["B", "A"], float_format=str)
biggie.to_string(columns=["B", "A"], col_space=12, float_format=str)

frame = DataFrame(index=np.arange(200))
frame.to_string()
