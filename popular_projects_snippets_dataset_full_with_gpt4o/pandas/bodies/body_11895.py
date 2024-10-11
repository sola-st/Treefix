# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
# GH#10261
data = """0
1
2
3
4
5
6
7
8
9
    """
df_iter = read_fwf(
    StringIO(data),
    colspecs=[(0, 2)],
    names=["a"],
    iterator=True,
    chunksize=2,
    skiprows=[0, 1, 2, 6, 9],
)
expected_frames = [
    DataFrame({"a": [3, 4]}),
    DataFrame({"a": [5, 7, 8]}, index=[2, 3, 4]),
    DataFrame({"a": []}, dtype="object"),
]
for i, result in enumerate(df_iter):
    tm.assert_frame_equal(result, expected_frames[i])
