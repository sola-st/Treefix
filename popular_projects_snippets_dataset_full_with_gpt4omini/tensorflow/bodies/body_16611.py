# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker.py
if isinstance(grad, tuple):
    grad = [grad]
error = 0
for j_t, j_n in grad:
    if j_t.size or j_n.size:  # Handle zero size tensors correctly
        error = np.maximum(error, np.fabs(j_t - j_n).max())
exit(error)
