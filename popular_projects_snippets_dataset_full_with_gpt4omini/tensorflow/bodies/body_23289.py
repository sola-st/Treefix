# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
super().tearDown()
os.environ["TF_TRT_ABORT_CUDA_ENGINE_BUILD"] = "False"
os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "False"
