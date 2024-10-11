# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
self.assertTrue(len(node.attr["calibration_data"].s), node.name)
