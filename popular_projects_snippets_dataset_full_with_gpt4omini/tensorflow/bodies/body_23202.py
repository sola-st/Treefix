# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/data_dependent_shape_test.py
super().setUp()
# The input shape depends on random input data. It can happen that we do
# not have engine for the actual shape. Therefore we enable native segment
# execution.
os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "True"
