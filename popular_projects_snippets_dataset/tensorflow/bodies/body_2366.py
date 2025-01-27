# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fused_batchnorm_test.py
# TODO(b/64270657): Use gradient_checker here in addition to comparing with
# this reference implementation.
channel = 3
x_shape = [2, 2, 6, channel]
scale_shape = [channel]
grad_val = np.random.random_sample(x_shape).astype(np.float32)
x_val = np.random.random_sample(x_shape).astype(np.float32)
scale_val = np.random.random_sample(scale_shape).astype(np.float32)
mean_val = np.random.random_sample(scale_shape).astype(np.float32)
var_val = np.random.random_sample(scale_shape).astype(np.float32)
data_format_src = "NHWC"

with self.session() as sess, self.test_scope():
    grad_val_converted = test_utils.ConvertBetweenDataFormats(
        grad_val, data_format_src, data_format)
    x_val_converted = test_utils.ConvertBetweenDataFormats(
        x_val, data_format_src, data_format)

    grad = array_ops.placeholder(
        np.float32, shape=x_val_converted.shape, name="grad")
    x = array_ops.placeholder(
        np.float32, shape=x_val_converted.shape, name="x")
    mean = array_ops.placeholder(np.float32, shape=scale_shape, name="mean")
    var = array_ops.placeholder(np.float32, shape=scale_shape, name="var")
    scale = array_ops.placeholder(np.float32, shape=scale_shape, name="scale")
    with self.test_scope():
        out = gen_nn_ops.fused_batch_norm_grad(
            grad,
            x,
            scale,
            mean,
            var,
            data_format=data_format,
            is_training=False)
        grad_x, grad_scale, grad_offset, _, _ = out

    ref_x, ref_scale, ref_offset, _, _ = gen_nn_ops.fused_batch_norm_grad(
        grad, x, scale, mean, var, data_format=data_format, is_training=False)

    grad_x_val, grad_scale_val, grad_offset_val, = sess.run(
        [grad_x, grad_scale, grad_offset], {
            grad: grad_val_converted,
            x: x_val_converted,
            mean: mean_val,
            var: var_val,
            scale: scale_val
        })
    grad_x_ref, grad_scale_ref, grad_offset_ref, = sess.run(
        [ref_x, ref_scale, ref_offset], {
            grad: grad_val_converted,
            x: x_val_converted,
            mean: mean_val,
            var: var_val,
            scale: scale_val
        })

    self.assertAllClose(grad_x_val, grad_x_ref, atol=1e-2)
    self.assertAllClose(grad_scale_val, grad_scale_ref, atol=1e-2)
    self.assertAllClose(grad_offset_val, grad_offset_ref, atol=1e-3)
