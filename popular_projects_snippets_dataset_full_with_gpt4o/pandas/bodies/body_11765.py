# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
warning_type = None
parser = all_parsers
size = 10000

# see gh-3866: if chunks are different types and can't
# be coerced using numerical types, then issue warning.
if parser.engine == "c" and parser.low_memory:
    warning_type = DtypeWarning
    # Use larger size to hit warning path
    size = 499999

integers = [str(i) for i in range(size)]
data = "a\n" + "\n".join(integers + ["a", "b"] + integers)

buf = StringIO(data)

df = parser.read_csv_check_warnings(
    warning_type,
    r"Columns \(0\) have mixed types. "
    "Specify dtype option on import or set low_memory=False.",
    buf,
)

assert df.a.dtype == object
