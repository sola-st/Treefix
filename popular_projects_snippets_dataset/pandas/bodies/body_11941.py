# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
data = "a,b,c\n1,2,3\n4,,"

result = TextReader(StringIO(data), delimiter=",").read()

expected = {
    0: np.array([1, 4], dtype=np.int64),
    1: np.array(["2", ""], dtype=object),
    2: np.array(["3", ""], dtype=object),
}
assert_array_dicts_equal(result, expected)

# GH5664
a = DataFrame([["b"], [np.nan]], columns=["a"], index=["a", "c"])
b = DataFrame([[1, 1, 1, 0], [1, 1, 1, 0]], columns=list("abcd"), index=[1, 1])
c = DataFrame(
    [
        [1, 2, 3, 4],
        [6, np.nan, np.nan, np.nan],
        [8, 9, 10, 11],
        [13, 14, np.nan, np.nan],
    ],
    columns=list("abcd"),
    index=[0, 5, 7, 12],
)

for _ in range(100):
    df = read_csv(StringIO("a,b\nc\n"), skiprows=0, names=["a"], engine="c")
    tm.assert_frame_equal(df, a)

    df = read_csv(
        StringIO("1,1,1,1,0\n" * 2 + "\n" * 2), names=list("abcd"), engine="c"
    )
    tm.assert_frame_equal(df, b)

    df = read_csv(
        StringIO("0,1,2,3,4\n5,6\n7,8,9,10,11\n12,13,14"),
        names=list("abcd"),
        engine="c",
    )
    tm.assert_frame_equal(df, c)
