# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH 39984
import pyarrow as pa

df = pd.DataFrame(
    {
        "a": Series([1, 2, None], dtype="Int64"),
        "b": pd.Float64Dtype().__from_arrow__(pa.array([0.2, np.nan, None])),
    }
)
multi_indexed = MultiIndex.from_frame(df)
expected = MultiIndex.from_arrays(
    [
        Series([1, 2, None]).astype("Int64"),
        pd.Float64Dtype().__from_arrow__(pa.array([0.2, np.nan, None])),
    ],
    names=["a", "b"],
)
tm.assert_index_equal(multi_indexed, expected)
