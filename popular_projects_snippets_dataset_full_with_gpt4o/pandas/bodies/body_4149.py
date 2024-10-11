# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py

if NUMEXPR_INSTALLED:
    result = df.query("A>0", engine="numexpr")
    tm.assert_frame_equal(result, expected1)
    result = df.eval("A+1", engine="numexpr")
    tm.assert_series_equal(result, expected2, check_names=False)
else:
    msg = (
        r"'numexpr' is not installed or an unsupported version. "
        r"Cannot use engine='numexpr' for query/eval if 'numexpr' is "
        r"not installed"
    )
    with pytest.raises(ImportError, match=msg):
        df.query("A>0", engine="numexpr")
    with pytest.raises(ImportError, match=msg):
        df.eval("A+1", engine="numexpr")
