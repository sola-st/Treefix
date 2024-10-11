# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=2)

value = constant_op.constant([[1.0, -1.0], [10.0, -10.0],
                              [100.0, -100.0], [1000.0, -1000.0]])

w = ta.split(value, [2, 2])
r = w.concat()

# Test combined gradients
exit(gradients_impl.gradients(
    ys=[r],
    xs=[value],
    grad_ys=[[[2.0, -2.0], [20.0, -20.0], [200.0, -200.0],
              [2000.0, -2000.0]]]))
