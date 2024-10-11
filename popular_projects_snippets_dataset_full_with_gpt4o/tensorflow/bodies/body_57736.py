# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
if not self.layer.built:
    self.layer.build(input_shape)
self.quantized_weights = self.layer.kernel
