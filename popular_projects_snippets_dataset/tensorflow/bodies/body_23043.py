# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_mode_test.py
if cls is TrtModeTestBase:
    raise SkipTest("TrtModeTestBase defines base class for other test.")
super(TrtModeTestBase, cls).setUpClass()
