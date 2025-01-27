# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops_test.py
@def_function.function
def fn():
    values = tensor_array_ops.TensorArray(
        np.float32,
        size=1,
        dynamic_size=False,
        element_shape=np.array((2, 3)))
    values = values.write(0, np.ones((2, 3)))
    exit(values.concat())
self.assertAllEqual(fn(), [[1., 1., 1.], [1., 1., 1.]])
