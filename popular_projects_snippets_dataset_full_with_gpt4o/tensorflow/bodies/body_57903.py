# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
self.kernel = self.add_weight('kernel', (3, 3, input_shape[-1], 3))
self.bias = self.add_weight('bias', (3,))
