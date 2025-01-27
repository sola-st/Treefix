# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
df = DataFrame([1, 2, 3])
assert not df.empty
df = DataFrame(index=[1], columns=[1])
assert not df.empty
df = DataFrame(index=["a", "b"], columns=["c", "d"]).dropna()
assert df.empty
assert df.T.empty
