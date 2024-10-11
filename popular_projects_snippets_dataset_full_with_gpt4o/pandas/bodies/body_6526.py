# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
# See https://github.com/pandas-dev/pandas/issues/29708
# Ensure that indexing operations do not materialize (convert to a numpy
# array) the ExtensionArray unnecessary

def DecimalArray__array__(self, dtype=None):
    raise Exception("tried to convert a DecimalArray to a numpy array")

monkeypatch.setattr(DecimalArray, "__array__", DecimalArray__array__, raising=False)

data = make_data()
s = pd.Series(DecimalArray(data))
df = pd.DataFrame({"a": s, "b": range(len(s))})

# ensure the following operations do not raise an error
s[s > 0.5]
df[s > 0.5]
s.at[0]
df.at[0, "a"]
