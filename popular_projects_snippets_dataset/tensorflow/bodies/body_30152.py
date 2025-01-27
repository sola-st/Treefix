# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):
    var = variables.Variable(
        array_ops.reshape(
            math_ops.range(1, 97, 1, dtype=dtypes.float32), shape=(6, 4, 4)))
    self.evaluate(var.initializer)

    raw = np.array(range(1, 97, 1)).reshape((6, 4, 4))
    grad = GradSliceChecker(self, var, raw, use_tape)
    _ = grad[2:6:2, 1:3, 1:3]
    _ = grad[3:0:-2, 1:3, 1:3]
    _ = grad[3:0:-2, array_ops.newaxis, 1:3, 2, array_ops.newaxis]
    _ = grad[3:0:-2, 1:3, 2]
    _ = grad[:, -1, :]
    _ = grad[:, -2, :]
    with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                                "out of bounds"):
        _ = grad[:, -200, :]
    with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                                "out of bounds"):
        _ = grad[:, 200, :]

    # Test numpy array type mask
    _ = grad[raw > 51]
    # Test tensor type mask
    _ = grad[ops.convert_to_tensor(raw) <= 76]
