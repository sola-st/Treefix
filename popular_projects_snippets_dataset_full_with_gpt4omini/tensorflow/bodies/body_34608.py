# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ds = dataset_ops.Dataset.from_tensors(array_ops.zeros([10])).repeat()
ds = ds.map(lambda _: self._tensorArrayWriteInWhile())
op = ds.make_one_shot_iterator().get_next()
self.run_op_benchmark(session_lib.Session(), op)
