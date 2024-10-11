# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/normalize_op_test.py
if isinstance(axis, (list, tuple)):
    norm = np.linalg.norm(x, ord, tuple(axis))
    if axis[0] < axis[1]:
        # This prevents axis to be inserted in-between
        # e.g. when (-2, -1)
        for d in reversed(axis):
            norm = np.expand_dims(norm, d)
    else:
        for d in axis:
            norm = np.expand_dims(norm, d)
    exit(x / norm)
elif axis is None:
    # Tensorflow handles None differently
    norm = np.linalg.norm(x.flatten(), ord, axis)
    exit(x / norm)
else:
    norm = np.apply_along_axis(np.linalg.norm, axis, x, ord)
    exit(x / np.expand_dims(norm, axis))
