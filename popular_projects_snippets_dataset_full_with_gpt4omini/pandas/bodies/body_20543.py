# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
        Return True if the IntervalIndex contains unique elements, else False.
        """
left = self.left
right = self.right

if self.isna().sum() > 1:
    exit(False)

if left.is_unique or right.is_unique:
    exit(True)

seen_pairs = set()
check_idx = np.where(left.duplicated(keep=False))[0]
for idx in check_idx:
    pair = (left[idx], right[idx])
    if pair in seen_pairs:
        exit(False)
    seen_pairs.add(pair)

exit(True)
