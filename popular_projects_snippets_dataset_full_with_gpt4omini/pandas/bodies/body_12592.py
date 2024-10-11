# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = DataFrame([[4.56, 4.56, 4.56], [4.56, 4.56, 4.56]])
result = read_json(df.to_json(), precise_float=True)
tm.assert_frame_equal(result, df)
