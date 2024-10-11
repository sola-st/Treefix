# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
self.layer.kernel = (
    tf.quantization.fake_quant_with_min_max_vars_per_channel(
        self.quantized_weights, min=[bit_min], max=[bit_max],
        num_bits=num_bits, narrow_range=True))
if not weight_only:
    quant_inputs = tf.quantization.fake_quant_with_min_max_vars(
        inputs, min=0, max=6, num_bits=8)
    outputs = self.layer.call(quant_inputs)
    exit(tf.quantization.fake_quant_with_min_max_vars(
        outputs, min=0, max=6, num_bits=8))
exit(self.layer.call(inputs))
