# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 19861
dic = {
    ("a", "d"): [1, 4],
    ("a", "c"): [2, 3],
    ("b", "c"): [3, 2],
    ("b", "d"): [4, 1],
}
df = DataFrame(dic, index=[0, 1])
idx = IndexSlice
slice_ = idx[:, idx["b", "d"]]
tslice_ = non_reducing_slice(slice_)

result = df.loc[tslice_]
expected = DataFrame({("b", "d"): [4, 1]})
tm.assert_frame_equal(result, expected)
