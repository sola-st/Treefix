# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
if context.executing_eagerly():
    with backprop.GradientTape() as tape:
        tape.watch([rt_val, default_val])
        out = rt_val.to_tensor(default_val, shape=shape_val)
        actual_rt_grad, actual_default_grad = tape.gradient(
            out, (rt_val, default_val), output_gradients=output_grad)
else:
    out = rt_val.to_tensor(default_val, shape=shape_val)
    actual_rt_grad, actual_default_grad = gradients_impl.gradients(
        ys=out, xs=(rt_val, default_val), grad_ys=output_grad)

self.assertAllClose(out, expected_output_val)
self.assertIsInstance(actual_rt_grad, RaggedTensor)
self.assertAllClose(actual_rt_grad, expected_rt_grad)
self.assertAllClose(actual_default_grad, expected_default_grad)
