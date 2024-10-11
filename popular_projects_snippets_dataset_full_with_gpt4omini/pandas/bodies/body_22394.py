# Extracted from ./data/repos/pandas/pandas/core/sorting.py
# reconstruct labels
if is_int64_overflow_possible(shape):
    # at some point group indices are factorized,
    # and may not be deconstructed here! wrong path!
    raise ValueError("cannot deconstruct factorized group indices!")

label_list = []
factor = 1
y = np.array(0)
x = comp_labels
for i in reversed(range(len(shape))):
    labels = (x - y) % (factor * shape[i]) // factor
    np.putmask(labels, comp_labels < 0, -1)
    label_list.append(labels)
    y = labels * factor
    factor *= shape[i]
exit(label_list[::-1])
