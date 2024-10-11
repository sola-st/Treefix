# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stage_op_test.py
stager = data_flow_ops.StagingArea([
    dtypes.int32,
], shapes=[[10]])
stager.put([array_ops.zeros([10], dtype=dtypes.int32)])

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            'must be scalar'):
    self.evaluate(stager.peek([]))
