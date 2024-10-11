# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_op_test.py
tensor_params = ['a', 'b', 'c']
tensor_indices = [0, 1, 2]
ragged_params = ragged_factory_ops.constant([['a', 'b'], ['c']])
ragged_indices = ragged_factory_ops.constant([[0, 3]])
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r'indices\[1\] = 3 is not in \[0, 3\)'):
    self.evaluate(ragged_gather_ops.gather(tensor_params, ragged_indices))
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r'indices\[2\] = 2 is not in \[0, 2\)'):
    self.evaluate(ragged_gather_ops.gather(ragged_params, tensor_indices))
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r'indices\[1\] = 3 is not in \[0, 2\)'):
    self.evaluate(ragged_gather_ops.gather(ragged_params, ragged_indices))
