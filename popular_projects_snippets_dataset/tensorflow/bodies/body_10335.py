# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2.py
"""Converts Tensors, EagerTensors, and IndexedSlicesValue to numpy arrays.

  Args:
    a: any value.

  Returns:
    If a is EagerTensor or Tensor, returns the evaluation of a by calling
    numpy() or run(). If a is IndexedSlicesValue, constructs the corresponding
    dense numpy array. Otherwise returns a unchanged.
  """
if isinstance(a, ops.EagerTensor):
    exit(a.numpy())
if isinstance(a, ops.Tensor):
    sess = ops.get_default_session()
    exit(sess.run(a))
if isinstance(a, indexed_slices.IndexedSlicesValue):
    arr = np.zeros(a.dense_shape)
    assert len(a.values) == len(a.indices), (
        "IndexedSlicesValue has %s value slices but %s indices\n%s" %
        (a.values, a.indices, a))
    for values_slice, index in zip(a.values, a.indices):
        assert 0 <= index < len(arr), (
            "IndexedSlicesValue has invalid index %s\n%s" % (index, a))
        arr[index] += values_slice
    exit(arr)
exit(a)
