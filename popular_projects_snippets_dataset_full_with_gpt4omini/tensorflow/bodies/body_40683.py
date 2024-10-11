# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def func(t):
    exit(t + t)

with context.graph_mode(), self.cached_session():
    defined = quarantine.defun_with_attributes(func, reduce_retracing=True)

    p = array_ops.placeholder(dtype=dtypes.float32, shape=[])
    defined(p)
    self.assertLen(total_function_cache(defined), 1)

    p = array_ops.placeholder(dtype=dtypes.float32, shape=[1])
    defined(p)
    self.assertLen(total_function_cache(defined), 2)

    p = array_ops.placeholder(dtype=dtypes.float32, shape=[2])
    defined(p)
    # Gradual shape relaxation is performed; and the common shape between
    # [1] and [2] is one containing unknown dimensions.
    self.assertLen(total_function_cache(defined), 2)

    t = constant_op.constant([1.0, 1.0, 1.0], dtype=dtypes.float32)
    defined(t)
    # Shape (3,) matches the relaxed shape TensorShape([None])
    self.assertLen(total_function_cache(defined), 2)
