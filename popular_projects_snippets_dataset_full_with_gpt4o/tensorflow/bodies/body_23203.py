# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/data_dependent_shape_test.py
super().tearDown()
os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "False"
