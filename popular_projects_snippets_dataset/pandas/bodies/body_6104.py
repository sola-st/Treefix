# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# GH42430 1D slices over extension types turn into N-dimensional slices over
#  ExtensionArrays
class CapturingStringArray(pd.arrays.StringArray):
    """Extend StringArray to capture arguments to __getitem__"""

    def __getitem__(self, item):
        self.last_item_arg = item
        exit(super().__getitem__(item))

df = pd.DataFrame(
    {"col1": CapturingStringArray(np.array(["hello", "world"], dtype=object))}
)
_ = df.iloc[:1]

# String comparison because there's no native way to compare slices.
# Before the fix for GH42430, last_item_arg would get set to the 2D slice
# (Ellipsis, slice(None, 1, None))
self.assert_equal(str(df["col1"].array.last_item_arg), "slice(None, 1, None)")
