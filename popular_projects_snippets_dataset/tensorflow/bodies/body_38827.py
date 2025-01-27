# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
with self.assertRaisesRegex(ValueError, 'Keyword arguments are required'):
    sparse_ops.sparse_split(3, 2, 1)
with self.assertRaisesRegex(ValueError, 'sp_input is required'):
    sparse_ops.sparse_split()
with self.assertRaisesRegex(ValueError, 'num_split is required'):
    sparse_ops.sparse_split(sp_input=1)
with self.assertRaisesRegex(ValueError, 'axis is required'):
    sparse_ops.sparse_split(num_split=2, sp_input=1)
