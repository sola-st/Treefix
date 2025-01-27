# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([2, 3, 5], dtype=np.int32),
    np.array([1], dtype=np.int32),
    expected=np.array([2, 3, 5], dtype=np.int32))

self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([1], dtype=np.int32),
    np.array([2, 3, 5], dtype=np.int32),
    expected=np.array([2, 3, 5], dtype=np.int32))

self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([2, 3, 5], dtype=np.int32),
    np.array([5], dtype=np.int32),
    expected=np.array([2, 3, 5], dtype=np.int32))

self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([5], dtype=np.int32),
    np.array([2, 3, 5], dtype=np.int32),
    expected=np.array([2, 3, 5], dtype=np.int32))

self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([2, 3, 5], dtype=np.int32),
    np.array([3, 5], dtype=np.int32),
    expected=np.array([2, 3, 5], dtype=np.int32))

self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([3, 5], dtype=np.int32),
    np.array([2, 3, 5], dtype=np.int32),
    expected=np.array([2, 3, 5], dtype=np.int32))

self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([2, 3, 5], dtype=np.int32),
    np.array([3, 1], dtype=np.int32),
    expected=np.array([2, 3, 5], dtype=np.int32))

self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([3, 1], dtype=np.int32),
    np.array([2, 3, 5], dtype=np.int32),
    expected=np.array([2, 3, 5], dtype=np.int32))

self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([2, 1, 5], dtype=np.int32),
    np.array([3, 1], dtype=np.int32),
    expected=np.array([2, 3, 5], dtype=np.int32))

self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([3, 1], dtype=np.int32),
    np.array([2, 1, 5], dtype=np.int32),
    expected=np.array([2, 3, 5], dtype=np.int32))

self._testBinary(
    array_ops.broadcast_dynamic_shape,
    np.array([2, 3, 5], dtype=np.int64),
    np.array([1], dtype=np.int64),
    expected=np.array([2, 3, 5], dtype=np.int64))
