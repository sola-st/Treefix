# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
exit(lambda: {
    'a':
        np.ones([1, 2, 3, 1]),
    'b':
        np.ones([1, 2, 3, 1, 5]),
    'c':
        ragged_factory_ops.constant(
            np.zeros([1, 2, 3, 1], dtype=np.uint8), dtype=dtypes.uint8),
    'd':
        ragged_factory_ops.constant(
            np.zeros([1, 2, 3, 1, 3]).tolist(), ragged_rank=1),
    'e':
        ragged_factory_ops.constant(
            np.zeros([1, 2, 3, 1, 2, 2]).tolist(), ragged_rank=2),
    'f':
        ragged_factory_ops.constant(
            np.zeros([1, 2, 3, 1, 3]), dtype=dtypes.float32),
    'g':
        StructuredTensor.from_pyval([[
            [  # pylint: disable=g-complex-comprehension
                [{
                    'x': j,
                    'y': k
                }] for k in range(3)
            ] for j in range(2)
        ]]),
    'h':
        StructuredTensor.from_pyval([[
            [  # pylint: disable=g-complex-comprehension
                [[
                    {
                        'x': j,
                        'y': k,
                        'z': z
                    } for z in range(j)
                ]] for k in range(3)
            ] for j in range(2)
        ]]),
})
