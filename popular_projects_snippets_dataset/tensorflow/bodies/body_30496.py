# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
indices = [0, 1, 2]
depth = 3
truth = np.asarray([[b"1.0", b"0.0", b"0.0"], [b"0.0", b"1.0", b"0.0"],
                    [b"0.0", b"0.0", b"1.0"]])
on_value = np.asarray(b"1.0")
off_value = np.asarray(b"0.0")

self._testBothOneHot(
    indices=indices,
    depth=depth,
    on_value=on_value,
    off_value=off_value,
    truth=truth)

on_value = constant_op.constant(b"1.0")
off_value = constant_op.constant(b"0.0")
self._testBothOneHot(
    indices=indices,
    depth=depth,
    on_value=on_value,
    off_value=off_value,
    truth=truth)

on_value = b"1.0"
off_value = b"0.0"
self._testBothOneHot(
    indices=indices,
    depth=depth,
    on_value=on_value,
    off_value=off_value,
    truth=truth)
