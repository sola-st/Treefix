# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
self.assertTrue(any(op_str in s.node_name for s in in_stats))
self.assertFalse(any(op_str in s.node_name for s in out_stats))
