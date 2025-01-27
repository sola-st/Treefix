# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fused_batchnorm_test.py
channel = 3
x_shape = [2, 2, 6, channel]
scale_shape = [channel]
x_val = np.random.random_sample(x_shape).astype(np.float32)
scale_val = np.random.random_sample(scale_shape).astype(np.float32)
offset_val = np.random.random_sample(scale_shape).astype(np.float32)
epsilon = 0.001
exponential_avg_factor = 1.0
data_format_src = "NHWC"
y_ref, mean_ref, var_ref, _ = self._reference_training(
    x_val, scale_val, offset_val, None, None, epsilon,
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
    y, mean, variance = nn.fused_batch_norm(
        t_val,
        scale,
        offset,
        mean=mean_ref,
        variance=var_ref,
        epsilon=epsilon,
        data_format=data_format,
        is_training=False)

    y_val, _, _ = sess.run([y, mean, variance], {
        t_val: x_val_converted,
        scale: scale_val,
        offset: offset_val
    })
    self.assertAllClose(y_val, y_ref_converted, atol=1e-3)
