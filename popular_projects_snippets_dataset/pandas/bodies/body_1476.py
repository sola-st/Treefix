# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH31340
df = DataFrame({"id": ["A"], "a": [1.2], "b": [0.0], "c": [-2.5]})
cols = ["a", "b", "c"]
df.loc[:, cols] = df.loc[:, cols].astype("float32")

# pre-2.0 this setting would swap in new arrays, in 2.0 it is correctly
#  in-place, consistent with non-split-path
expected = DataFrame(
    {
        "id": ["A"],
        "a": np.array([1.2], dtype="float64"),
        "b": np.array([0.0], dtype="float64"),
        "c": np.array([-2.5], dtype="float64"),
    }
)  # id is inferred as object

tm.assert_frame_equal(df, expected)
