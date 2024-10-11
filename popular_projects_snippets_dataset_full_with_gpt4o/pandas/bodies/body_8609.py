# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_join.py
df = tm.makeCustomDataframe(
    10,
    10,
    data_gen_f=lambda *args: np.random.randint(2),
    c_idx_type="p",
    r_idx_type="dt",
)
s = df.iloc[:5, 0]

expected = df.columns.astype("O").join(s.index, how=join_type)
result = df.columns.join(s.index, how=join_type)
tm.assert_index_equal(expected, result)
