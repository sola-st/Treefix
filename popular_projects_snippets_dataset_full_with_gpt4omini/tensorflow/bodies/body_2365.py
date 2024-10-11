# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fused_batchnorm_test.py
# disable_mlir_bridge for GPUs as there is no legalization for GPU with
# MLIR.
# TODO(b/189039456): Customize FusedBatchNorm legalization for GPU in MLIR.
if test_util.is_mlir_bridge_enabled() and self.device == "XLA_GPU":
    self.skipTest("b/189039456")

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
epsilon = 0.001

# The TensorFlow FusedBatchNormGrad training operation takes two inputs with
# implementation defined values.  In theory the only correct value these
# inputs are the corresponding reserve_space_{1|2} outputs from the
# FusedBatchNorm training operation.  However, in practice, we rely on the
# first one being mean on {C|G}PU, and the second one being variance on CPU
# and inverse(sqrt(variance + epsilon)) on GPU (we test this assumption
# separately).
reserve_space_1_val = mean_val
if self.device == "XLA_GPU":
    reserve_space_2_val = np.reciprocal(np.sqrt(var_val + epsilon))
else:
    reserve_space_2_val = var_val

data_format_src = "NHWC"
grad_x_ref, grad_scale_ref, grad_offset_ref = self._reference_grad(
    x_val, grad_val, scale_val, mean_val, var_val, epsilon, data_format_src)

with self.session() as sess, self.test_scope():
    grad_val_converted = test_utils.ConvertBetweenDataFormats(
        grad_val, data_format_src, data_format)
    x_val_converted = test_utils.ConvertBetweenDataFormats(
        x_val, data_format_src, data_format)
    grad_x_ref_converted = test_utils.ConvertBetweenDataFormats(
        grad_x_ref, data_format_src, data_format)

    grad = array_ops.placeholder(
        np.float32, shape=x_val_converted.shape, name="grad")
    x = array_ops.placeholder(
        np.float32, shape=x_val_converted.shape, name="x")
    reserve_space_1 = array_ops.placeholder(
        np.float32, shape=scale_shape, name="reserve_space_1")
    reserve_space_2 = array_ops.placeholder(
        np.float32, shape=scale_shape, name="reserve_space_2")
    scale = array_ops.placeholder(np.float32, shape=scale_shape, name="scale")
    grad_x, grad_scale, grad_offset, _, _ = gen_nn_ops.fused_batch_norm_grad(
        grad,
        x,
        scale,
        reserve_space_1,
        reserve_space_2,
        data_format=data_format,
        is_training=True)

    grad_x_val, grad_scale_val, grad_offset_val = sess.run(
        [grad_x, grad_scale, grad_offset], {
            grad: grad_val_converted,
            x: x_val_converted,
            reserve_space_1: reserve_space_1_val,
            reserve_space_2: reserve_space_2_val,
            scale: scale_val
        })

    self.assertAllClose(grad_x_val, grad_x_ref_converted, atol=1e-2)
    self.assertAllClose(grad_scale_val, grad_scale_ref, atol=1e-2)
    self.assertAllClose(grad_offset_val, grad_offset_ref, atol=1e-3)
