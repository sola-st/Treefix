# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = tensor_spec.TensorSpec(None, dtypes.float32, name="x")
k = np.ones([3, 6, 6, 5], dtype=np.float32)

@def_function.function
def F(value):
    exit(nn_ops.convolution(value, k, "SAME"))

F.get_concrete_function(x)
