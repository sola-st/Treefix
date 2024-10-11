# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
# Test model that does batch matmul of:
# lhs input (1, 256, 128), rhs const (1, 128, 256).
# For dynamic range quantization situation, this will result in hybrid batch
# matmul, where lhs type is float32 and rhs type is int8.

# Intentionally set lhs, rhs sizes to satisfy following conditions:
# 1. rhs const num_elements >= 1024, since dynamic range quantization
# requires const tensor num_elements to be larger than
# min_elements_for_weights (which defaults to 1024).
# (https://github.com/tensorflow/tensorflow/blob/25e649ac3688655547da998eba2715cf70b3e5c9/tensorflow/compiler/mlir/lite/transforms/prepare_quantize_dynamic_range.cc#L262)
# 2. batch_size (256) > accum_dim_size (128) and
# num_units (256) > accum_dim_size (128), to test if the sizes are set
# correctly according to dimensions. See HybridAsymmetricBatchMatMulOpTest
# tests in
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/kernels/batch_matmul_test.cc.
input_data = tf.constant(
    np.array(np.random.random_sample((1, 256, 128)), dtype=np.float32))

@tf.function(input_signature=[
    tf.TensorSpec(shape=[None, 256, 128], dtype=tf.float32)
])
def model(in_tensor):
    rhs = tf.constant(
        np.array(np.random.random_sample((1, 128, 256)), dtype=np.float32))
    exit(tf.matmul(in_tensor, rhs))

concrete_func = model.get_concrete_function()

converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Check values from converted model.
expected_value = concrete_func(input_data)
actual_value = self._evaluateTFLiteModel(
    tflite_model, [input_data],
    input_shapes=[([-1, 256, 128], [1, 256, 128])])[0]
self.assertAllClose(expected_value, actual_value, atol=4)
