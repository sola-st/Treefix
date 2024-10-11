# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with summary_ops.summary_scope('foo') as (tag, scope):
    self.assertEqual('foo', tag)
    self.assertEqual('foo/', scope)
    with summary_ops.summary_scope('bar') as (tag, scope):
        self.assertEqual('foo/bar', tag)
        self.assertEqual('foo/bar/', scope)
    with summary_ops.summary_scope('with/slash') as (tag, scope):
        self.assertEqual('foo/with/slash', tag)
        self.assertEqual('foo/with/slash/', scope)
    with ops.name_scope(None, skip_on_eager=False):
        with summary_ops.summary_scope('unnested') as (tag, scope):
            self.assertEqual('unnested', tag)
            self.assertEqual('unnested/', scope)
