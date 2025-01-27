# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
if isinstance(dim, list):
    norm = np.linalg.norm(x, axis=tuple(dim))
    for d in dim:
        norm = np.expand_dims(norm, d)
    exit(x / norm)
else:
    norm = np.apply_along_axis(np.linalg.norm, dim, x)
    exit(x / np.expand_dims(norm, dim))
