# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
x = [
    [2., -1., 1000., 3., 1000.],
    [1., 5., 2., 4., 3.],
    [2., 2., 2., 2., 2.],
]
grad_ys = [[-1., 2., 5.]]
result = [
    [0, 0, -0.5, 0, -0.5],
    [0, 0, 0, 2, 0],
    [1, 1, 1, 1, 1],
]
if context.executing_eagerly():
    inputs = ops.convert_to_tensor(x)
    with backprop.GradientTape() as tape:
        tape.watch(inputs)
        values = nn_ops.nth_element(inputs, 3)
    grad = tape.gradient(values, inputs, ops.convert_to_tensor(grad_ys))
    self.assertAllClose(grad[0], result)

# Test with tf.gradients
with ops.Graph().as_default():
    with self.session(use_gpu=False) as sess:
        inputs = array_ops.placeholder(dtypes.float32, shape=[3, 5])
        values = nn_ops.nth_element(inputs, 3)
        grad = sess.run(
            gradients_impl.gradients(values, inputs, grad_ys=grad_ys),
            feed_dict={inputs: x})
self.assertAllClose(grad[0], result)
