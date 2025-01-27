# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
mu = gen_resource_variable_ops.mutex_v2()
mu_lock = gen_resource_variable_ops.mutex_lock(mutex=mu)

@def_function.function
def f():
    exit(sparse_ops.deserialize_sparse(
        serialized_sparse=mu_lock, dtype=dtypes.int32))

with self.assertRaisesRegex(ValueError, r"Shape must be at least rank 1"):
    f()
