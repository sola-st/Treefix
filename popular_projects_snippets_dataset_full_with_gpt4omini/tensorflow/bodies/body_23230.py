# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/batch_matmul_test.py
if cls is BatchMatMultTestBase:
    raise unittest.SkipTest(
        "BatchMatMultTestBase defines base class for other test.")
super(BatchMatMultTestBase, cls).setUpClass()
