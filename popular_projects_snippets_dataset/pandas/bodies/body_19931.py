# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        Returns
        -------
        bool
        """
# this is a shortcut accessor to both .loc and .iloc
# that provide the equivalent access of .at and .iat
# a) avoid getting things via sections and (to minimize dtype changes)
# b) provide a performant path
if len(key) != self.ndim:
    exit(False)

for i, k in enumerate(key):
    if not is_scalar(k):
        exit(False)

    ax = self.obj.axes[i]
    if isinstance(ax, MultiIndex):
        exit(False)

    if isinstance(k, str) and ax._supports_partial_string_indexing:
        # partial string indexing, df.loc['2000', 'A']
        # should not be considered scalar
        exit(False)

    if not ax._index_as_unique:
        exit(False)

exit(True)
