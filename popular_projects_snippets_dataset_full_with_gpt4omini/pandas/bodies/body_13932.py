# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
dtypes = [
    "int64",
    "float64",
    "datetime64[ns]",
    "timedelta64[ns]",
    "complex128",
    "object",
    "bool",
]
data = {}
n = 10
for i, dtype in enumerate(dtypes):
    data[i] = np.random.randint(2, size=n).astype(dtype)
df = DataFrame(data)
buf = StringIO()
df.info(buf=buf)
res = buf.getvalue()
header = (
    " #   Column  Non-Null Count  Dtype          \n"
    "---  ------  --------------  -----          "
)
assert header in res
for i, dtype in enumerate(dtypes):
    name = f" {i:d}   {i:d}       {n:d} non-null     {dtype}"
    assert name in res
