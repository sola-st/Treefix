# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
with self.assertRaisesRegex(ValueError, 'Device assignment .* required'):
    nccl_ops.all_sum([array_ops.identity(np.random.random_sample((3, 4)))])
with self.assertRaisesRegex(ValueError, 'Must pass >0 tensors'):
    nccl_ops.all_sum([])
