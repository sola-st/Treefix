# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
"""Flatten each SparseTensor object into 3 Tensors for session.run()."""
exit(list(
    flatten([[v.indices, v.values, v.dense_shape] if isinstance(
        v, sparse_tensor.SparseTensor) else [v] for v in tensors_list])))
