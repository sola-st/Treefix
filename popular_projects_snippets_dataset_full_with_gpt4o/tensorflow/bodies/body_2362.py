# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fused_batchnorm_test.py
channel = 3
x_shape = [2, 2, 6, channel]
scale_shape = [channel]
x_val = np.random.random_sample(x_shape).astype(np.float32)
scale_val = np.random.random_sample(scale_shape).astype(np.float32)
offset_val = np.random.random_sample(scale_shape).astype(np.float32)
mean_val = np.random.random_sample(scale_shape).astype(np.float32)
var_val_corr = np.random.random_sample(scale_shape).astype(np.float32)
epsilon = 0.001
data_format_src = "NHWC"
# When in training mode, fused_batchnorm applies an implicit Bessel's
# correction. So we have to use the corrected variance here, as well.
y_ref, mean_ref, _, var_ref_corr = self._reference_training(
    x_val, scale_val, offset_val, mean_val, var_val_corr, epsilon,
    exponential_avg_factor, data_format_src)

with self.session() as sess, self.test_scope():
    # To avoid constant folding
    x_val_converted = test_utils.ConvertBetweenDataFormats(
        x_val, data_format_src, data_format)
    y_ref_converted = test_utils.ConvertBetweenDataFormats(
        y_ref, data_format_src, data_format)

    t_val = array_ops.placeholder(
        np.float32, shape=x_val_converted.shape, name="x")
    scale = array_ops.placeholder(np.float32, shape=scale_shape, name="scale")
    offset = array_ops.placeholder(
        np.float32, shape=scale_shape, name="offset")
    if exponential_avg_factor == 1.0:
        old_mean = None
        old_var = None
    else:
        old_mean = array_ops.placeholder(
            np.float32, shape=scale_shape, name="old_mean")
        old_var = array_ops.placeholder(
            np.float32, shape=scale_shape, name="old_var")
    y, mean, var = nn.fused_batch_norm(
        t_val,
        scale,
        offset,
        mean=old_mean,
        variance=old_var,
        epsilon=epsilon,
        exponential_avg_factor=exponential_avg_factor,
        data_format=data_format,
        is_training=True)
    if exponential_avg_factor == 1.0:
        feed_dict = {
            t_val: x_val_converted,
            scale: scale_val,
            offset: offset_val,
        }
    else:
        feed_dict = {
            t_val: x_val_converted,
            scale: scale_val,
            offset: offset_val,
            old_mean: mean_val,
            old_var: var_val_corr
        }
    # Check gradient.
    if use_gradient_checker:
        err = gradient_checker.compute_gradient_error(
            t_val,
            x_val_converted.shape,
            y,
            x_val_converted.shape,
            extra_feed_dict=feed_dict)
        self.assertLess(err, 1e-3)

    y_tf, mean_tf, var_tf = sess.run([y, mean, var], feed_dict)
    self.assertAllClose(y_tf, y_ref_converted, atol=1e-3)
    self.assertAllClose(mean_tf, mean_ref, atol=1e-3)
    self.assertAllClose(var_tf, var_ref_corr, atol=1e-3)
