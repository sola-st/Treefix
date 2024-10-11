# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
with dist.scope():
    with self.assertRaises(_TestException):
        dist.extended.call_for_each_replica(_raise_exception_fn)
    with self.assertRaises(_TestException):
        dist.extended.call_for_each_replica(_merge_raises_fn)
    with self.assertRaises(_TestException):
        dist.extended.call_for_each_replica(_merge_call_raises_fn)
    with self.assertRaises(_TestException):
        dist.extended.call_for_each_replica(_merge_call_merge_raises_fn)
