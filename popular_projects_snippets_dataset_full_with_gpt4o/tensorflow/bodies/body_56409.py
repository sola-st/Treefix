# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
context.context().configure_collective_ops(
    collective_leader='/job:worker/replica:0/task:0',
    scoped_allocator_enabled_ops=('CollectiveReduce',),
    use_nccl_communication=False,
    device_filters=['/job:worker/task:1'])
new_config = context.context().config

# Verify group leader
self.assertEqual('/job:worker/replica:0/task:0',
                 new_config.experimental.collective_group_leader)

# Verify device filters.
self.assertEqual(['/job:worker/task:1'], new_config.device_filters)

# Verify rewrite options.
new_rewrite_options = new_config.graph_options.rewrite_options
self.assertEqual(rewriter_config_pb2.RewriterConfig.ON,
                 new_rewrite_options.scoped_allocator_optimization)
self.assertEqual(['CollectiveReduce'],
                 new_rewrite_options.scoped_allocator_opts.enable_op)
