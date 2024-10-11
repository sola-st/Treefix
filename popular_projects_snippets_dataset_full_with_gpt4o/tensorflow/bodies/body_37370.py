# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with summary_ops.summary_scope(None) as (tag, scope):
    self.assertEqual('summary', tag)
    self.assertEqual('summary/', scope)
with summary_ops.summary_scope(None, 'backup') as (tag, scope):
    self.assertEqual('backup', tag)
    self.assertEqual('backup/', scope)
