# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
filepath = datapath("io", "parser", "data", "unicode_series.csv")
df = read_csv(filepath, header=None, encoding="latin1")
repr(df)
repr(df[1])
