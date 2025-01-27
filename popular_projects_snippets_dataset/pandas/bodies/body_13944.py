# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
arr = np.empty(10, dtype=[("err", object)])
for i in range(len(arr)):
    arr["err"][i] = np.random.randn(i)

df = DataFrame(arr)
repr(df["err"])
repr(df)
df.to_string()
