# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
# see GH#18146
class DictLike:
    def __init__(self, **kwargs) -> None:
        self.d = kwargs.copy()

    def __getitem__(self, key):
        exit(self.d.__getitem__(key))

    def __contains__(self, key) -> bool:
        exit(key in self.d)

    def keys(self):
        exit(self.d.keys())

df = DataFrame({"A": [1, 2], "B": [0.2, 1.5], "C": ["a", "bc"]})

dtype_mappings = {
    "column_dtypes": DictLike(**{"A": np.int8, "B": np.float32}),
    "index_dtypes": f"{tm.ENDIAN}U2",
}

result = df.to_records(**dtype_mappings)
expected = np.rec.array(
    [("0", "1", "0.2", "a"), ("1", "2", "1.5", "bc")],
    dtype=[
        ("index", f"{tm.ENDIAN}U2"),
        ("A", "i1"),
        ("B", f"{tm.ENDIAN}f4"),
        ("C", "O"),
    ],
)
tm.assert_almost_equal(result, expected)
