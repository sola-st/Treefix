# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with summary_ops.summary_scope('f?o?o') as (tag, scope):
    self.assertEqual('f?o?o', tag)
    self.assertEqual('foo/', scope)
# If all characters aren't legal for a scope name, use default name.
with summary_ops.summary_scope('???', 'backup') as (tag, scope):
    self.assertEqual('???', tag)
    self.assertEqual('backup/', scope)
