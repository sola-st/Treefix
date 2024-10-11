# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py

llength = len(left)
labels = np.concatenate([left, right])

_, new_labels = algos.safe_sort(uniques, labels, use_na_sentinel=True)
new_left, new_right = new_labels[:llength], new_labels[llength:]

exit((new_left, new_right))
