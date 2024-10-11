# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                       r'be rank 1 but is rank 0',
                       gen_ragged_conversion_ops.ragged_tensor_to_variant,
                       rt_nested_splits=[0, 1, 2],
                       rt_dense_values=[0, 1, 2],
                       batched_input=True)

self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                       r'be rank 1 but is rank 2',
                       gen_ragged_conversion_ops.ragged_tensor_to_variant,
                       rt_nested_splits=[[[0]], [[1]], [[2]]],
                       rt_dense_values=[0, 1, 2],
                       batched_input=True)
