# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
super(TensorArrayTest, cls).tearDownClass()
session_lib.Session.reset(cls._workers[0].target)
