# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_select_dtypes.py
# GH 11990
df = tm.makeCustomDataframe(30, 3, data_gen_f=lambda x, y: np.random.random())
expected = df
FLOAT_TYPES = list(np.typecodes["AllFloat"])
tm.assert_frame_equal(df.select_dtypes(FLOAT_TYPES), expected)
