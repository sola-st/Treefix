# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
# see gh-19038
df = DataFrame(
    [1, 2, 3], ["2016-01-01", "2017-01-01", "2018-01-01"], columns=["a"]
)
df.index = pd.to_datetime(df.index)
on_vector = df.index.year

if box is not None:
    on_vector = box(on_vector)

exp_years = np.array([2016, 2017, 2018], dtype=np.int32)
expected = DataFrame({"a": [1, 2, 3], "key_1": exp_years})

result = df.merge(df, on=["a", on_vector], how="inner")
tm.assert_frame_equal(result, expected)

expected = DataFrame({"key_0": exp_years, "a_x": [1, 2, 3], "a_y": [1, 2, 3]})

result = df.merge(df, on=[df.index.year], how="inner")
tm.assert_frame_equal(result, expected)
