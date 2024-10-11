# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
df = pd.DataFrame({"A": pd.array(["a", pd.NA, "b"], dtype=dtype)})
expected = "      A\n0     a\n1  <NA>\n2     b"
assert repr(df) == expected

expected = "0       a\n1    <NA>\n2       b\nName: A, dtype: string"
assert repr(df.A) == expected

arr_name = "ArrowStringArray" if dtype.storage == "pyarrow" else "StringArray"
expected = f"<{arr_name}>\n['a', <NA>, 'b']\nLength: 3, dtype: string"
assert repr(df.A.array) == expected
