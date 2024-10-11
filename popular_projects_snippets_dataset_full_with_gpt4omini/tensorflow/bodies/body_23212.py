# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/vgg_block_nchw_test.py
super().setUp()
os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "True"
