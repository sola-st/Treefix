# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
super(TensorArrayTest, cls).setUpClass()
cls._workers, _ = test.create_local_cluster(num_workers=3, num_ps=0)
