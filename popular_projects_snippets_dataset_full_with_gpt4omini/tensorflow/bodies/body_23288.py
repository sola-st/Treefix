# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
super().setUp()
# This is to test whether shape value mask is correctly set in case engine
# construction has failed.
os.environ["TF_TRT_ABORT_CUDA_ENGINE_BUILD"] = "True"
os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "True"
