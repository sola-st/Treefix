# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
with self.cached_session():
    num_inputs = np.prod(input_shape)
    num_grads = np.prod(slice_size)
    inp = np.random.rand(num_inputs).astype("f").reshape(input_shape)
    a = constant_op.constant(
        [float(x) for x in inp.ravel(order="C")],
        shape=input_shape,
        dtype=dtypes.float32)
    slice_t = array_ops.slice(a, slice_begin, slice_size)
    grads = np.random.rand(num_grads).astype("f").reshape(slice_size)
    grad_tensor = constant_op.constant(grads)
    grad = gradients_impl.gradients(slice_t, [a], grad_tensor)[0]
    result = self.evaluate(grad)

# Create a zero tensor of the input shape ane place
# the grads into the right location to compare against TensorFlow.
np_ans = np.zeros(input_shape)
slices = []
for i in range(len(input_shape)):
    slices.append(slice(slice_begin[i], slice_begin[i] + slice_size[i]))
np_ans[tuple(slices)] = grads

self.assertAllClose(np_ans, result)
