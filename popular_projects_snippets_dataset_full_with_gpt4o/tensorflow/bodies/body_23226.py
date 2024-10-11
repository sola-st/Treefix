# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/biasadd_matmul_test.py
super().setUp()
# Disable layout optimizer, since it will convert BiasAdd with NHWC
# format to NCHW format under four dimentional input.
self.DisableNonTrtOptimizers()
