# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/annotate_max_batch_sizes_test.py
if cls is MaxBatchSizesTestBase:
    raise unittest.SkipTest(
        'MaxBatchSizesTestBase defines base class for other tests.')
super(MaxBatchSizesTestBase, cls).setUpClass()
