# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
super(CollectiveAllReduceTest, self).setUp()
# Reusing keys is not supported well. So we have to give a different
# collective key base for different tests.
CollectiveAllReduceTest.collective_key_base += 100000
mwms_lib.CollectiveAllReduceStrategy._collective_key_base = (
    CollectiveAllReduceTest.collective_key_base)
