# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ops.reset_default_graph()
op = self._tensorArrayWriteInWhile()
self.run_op_benchmark(session_lib.Session(), op)
