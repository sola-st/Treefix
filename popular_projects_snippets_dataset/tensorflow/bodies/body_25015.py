# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
counts = [len(np.shape(arr)), np.size(arr), 0, 0, 0, 0, 0, 0]
for n in np.ravel(arr):
    if np.isneginf(n):
        counts[2] += 1
    elif np.isposinf(n):
        counts[3] += 1
    elif np.isnan(n):
        counts[4] += 1
    elif n < 0.:
        counts[5] += 1
    elif n == 0.:
        counts[6] += 1
    else:
        counts[7] += 1
exit(counts)
