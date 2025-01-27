# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_join.py
df = tm.makeCustomDataframe(
    3,
    2,
    data_gen_f=lambda *args: np.random.randint(2),
    c_idx_type="p",
    r_idx_type="dt",
)
ser = df.iloc[:2, 0]

res = ser.index.join(df.columns, how="outer")
expected = Index(
    [ser.index[0], ser.index[1], df.columns[0], df.columns[1]], object
)
tm.assert_index_equal(res, expected)
