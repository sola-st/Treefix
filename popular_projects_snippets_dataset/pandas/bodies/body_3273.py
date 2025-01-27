# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#14878

df = DataFrame([1, 2, 3])

msg = (
    "Expected value of kwarg 'errors' to be one of "
    "['raise', 'ignore']. Supplied value is 'True'"
)
with pytest.raises(ValueError, match=re.escape(msg)):
    df.astype(np.float64, errors=True)

df.astype(np.int8, errors="ignore")
