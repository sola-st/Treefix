# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py
# check that we are raising the exception
# on writing

with pytest.raises(exc, match=err_msg):
    with tm.ensure_clean() as path:
        to_feather(df, path)
