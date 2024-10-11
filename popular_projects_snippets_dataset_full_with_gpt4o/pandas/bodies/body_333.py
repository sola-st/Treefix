# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 8664
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df_orig = df.copy()
msg = "cannot assign without a target object"
with pytest.raises(ValueError, match=msg):
    df.query("a = 1")
tm.assert_frame_equal(df, df_orig)
