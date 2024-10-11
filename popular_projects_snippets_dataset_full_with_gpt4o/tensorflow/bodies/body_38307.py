# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
assert mode in ("sum", "mean", "sqrtn")
if mode != "sum":
    weights = np.zeros(ygrad.shape[0], ygrad.dtype)
    for segment in segment_ids:
        weights[segment] += 1
    weights = 1. / weights if mode == "mean" else 1. / np.sqrt(weights)
xgrad = np.zeros([output_dim0, ygrad.shape[1]], ygrad.dtype)
for segment, index in zip(segment_ids, indices):
    if mode == "sum":
        xgrad[index] += ygrad[segment]
    else:
        xgrad[index] += ygrad[segment] * weights[segment]
exit(xgrad)
