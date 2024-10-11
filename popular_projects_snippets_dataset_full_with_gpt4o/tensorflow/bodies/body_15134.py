# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = [[[1], [2], [3]], [[4], [5], [6]]]

rt1 = RaggedTensor.from_tensor(rt, ragged_rank=1)
rt1._set_shape([2, 3, 1])

rt2 = nest.map_structure(
    lambda x: array_ops.placeholder_with_default(x, None),
    rt1,
    expand_composites=True)
rt2._set_shape([2, 3, 1])
