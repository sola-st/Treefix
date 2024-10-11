# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
np.random.seed(123)
x = np.random.randn(3)
df = DataFrame(
    {
        "A1970": {0: "a", 1: "b", 2: "c"},
        "A1980": {0: "d", 1: "e", 2: "f"},
        "B1970": {0: 2.5, 1: 1.2, 2: 0.7},
        "B1980": {0: 3.2, 1: 1.3, 2: 0.1},
        "X": dict(zip(range(3), x)),
    }
)
df["id"] = df.index
exp_data = {
    "X": x.tolist() + x.tolist(),
    "A": ["a", "b", "c", "d", "e", "f"],
    "B": [2.5, 1.2, 0.7, 3.2, 1.3, 0.1],
    "year": [1970, 1970, 1970, 1980, 1980, 1980],
    "id": [0, 1, 2, 0, 1, 2],
}
expected = DataFrame(exp_data)
expected = expected.set_index(["id", "year"])[["X", "A", "B"]]
result = wide_to_long(df, ["A", "B"], i="id", j="year")
tm.assert_frame_equal(result, expected)
