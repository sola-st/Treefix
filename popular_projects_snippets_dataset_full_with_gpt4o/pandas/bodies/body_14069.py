# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
index = ["'Til There Was You (1997)", "ldum klaka (Cold Fever) (1994)"]
fmt.set_option("display.max_rows", 1)
df = DataFrame(columns=["a", "b", "c"], index=index)
repr(df)
repr(df.T)
fmt.set_option("display.max_rows", 200)
