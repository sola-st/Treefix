# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# If all stubs names end with a string, but a numeric suffix is
# assumed,  an empty data frame is returned
df = DataFrame(
    {
        "Aone": [1.0, 2.0],
        "Atwo": [3.0, 4.0],
        "Bone": [5.0, 6.0],
        "X": ["X1", "X2"],
    }
)
df["id"] = df.index
exp_data = {
    "X": "",
    "Aone": [],
    "Atwo": [],
    "Bone": [],
    "id": [],
    "year": [],
    "A": [],
    "B": [],
}
expected = DataFrame(exp_data).astype({"year": np.int64})

expected = expected.set_index(["id", "year"])
expected.index = expected.index.set_levels([0, 1], level=0)
result = wide_to_long(df, ["A", "B"], i="id", j="year")
tm.assert_frame_equal(result.sort_index(axis=1), expected.sort_index(axis=1))
