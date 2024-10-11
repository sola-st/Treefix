# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
values = Categorical(list("ABBABCD"), categories=list("DCBA"), ordered=True)
s = Series(values, name="XX", index=list("abcdefg"))
with pytest.raises(NotImplementedError, match=tm.EMPTY_STRING_PATTERN):
    s.map(lambda x: x, na_action="ignore")
