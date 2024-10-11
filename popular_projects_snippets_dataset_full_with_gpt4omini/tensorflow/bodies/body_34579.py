# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py

def ta_gather(indices):
    ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=3)
    x = constant_op.constant([1.0, 2.0, 3.0])
    ta = ta.write(0, x)
    t = ta.gather(indices)
    self.assertEqual(t.shape.as_list(), [first_dim, 3])
    exit(t)

# This propagates shape of `indices` when compiling ta_gather.
ta_gather_with_known_indices_shape = def_function.function(ta_gather)
first_dim = 1
ta_gather_with_known_indices_shape([0])

# Here were force the shape of `indices` to be [None] during ta_gather's
# compilation.
ta_gather_with_unknown_indices_shape = def_function.function(
    ta_gather,
    input_signature=[
        tensor_spec.TensorSpec(dtype=dtypes.int32, shape=[None])
    ])
first_dim = None
ta_gather_with_unknown_indices_shape([0])
