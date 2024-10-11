# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# 11320
df = DataFrame(
    {
        "rna": (1.5, 2.2, 3.2, 4.5),
        -1000: [11, 21, 36, 40],
        0: [10, 22, 43, 34],
        1000: [0, 10, 20, 30],
    },
    columns=["rna", -1000, 0, 1000],
)
result = df[[1000]]
expected = df.iloc[:, [3]]
tm.assert_frame_equal(result, expected)
result = df[[-1000]]
expected = df.iloc[:, [1]]
tm.assert_frame_equal(result, expected)
