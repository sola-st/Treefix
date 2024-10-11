# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
tf_types = [dtypes.uint8, dtypes.int32, dtypes.int64]
np_types = [np.int32, np.int64]
for itype in tf_types + np_types:
    # Note: to keep the tests simple in the case of uint8 the index -1 below
    # maps to 255 which is out of the depth range, just like -1.
    if itype in tf_types:
        indices = constant_op.constant(
            [[0, 2, -1, 1], [1, 0, 1, -1]], dtype=itype)
    elif itype in np_types:
        indices = np.asarray([[0, 2, -1, 1], [1, 0, 1, -1]], dtype=itype)
    depth = 3

    on_value = np.asarray(1.0, dtype=np.float32)
    off_value = np.asarray(-1.0, dtype=np.float32)

    truth = np.asarray(
        [[[1.0, -1.0, -1.0], [-1.0, -1.0, 1.0], [-1.0, -1.0, -1.0],
          [-1.0, 1.0, -1.0]], [[-1.0, 1.0, -1.0], [1.0, -1.0, -1.0],
                               [-1.0, 1.0, -1.0], [-1.0, -1.0, -1.0]]],
        dtype=np.float32)

    # axis == -1
    self._testBothOneHot(
        indices=indices,
        on_value=on_value,
        off_value=off_value,
        depth=depth,
        truth=truth)

    # axis == 1
    self._testBothOneHot(
        indices=indices,
        on_value=on_value,
        off_value=off_value,
        depth=depth,
        axis=1,
        truth=[truth[0].T, truth[1].T])  # Do not transpose the batch
