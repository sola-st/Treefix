# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
constant_op.constant(0, name='foo')
with summary_ops.summary_scope('foo') as (tag, _):
    self.assertEqual('foo', tag)
with summary_ops.summary_scope('foo') as (tag, _):
    self.assertEqual('foo', tag)
with ops.name_scope('with', skip_on_eager=False):
    constant_op.constant(0, name='slash')
with summary_ops.summary_scope('with/slash') as (tag, _):
    self.assertEqual('with/slash', tag)
