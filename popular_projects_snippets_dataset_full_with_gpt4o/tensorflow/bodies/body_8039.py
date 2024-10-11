# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
strategy, _ = self._get_test_object(
    task_type='worker', task_id=1, num_gpus=2)

config_proto = config_pb2.ConfigProto(device_filters=['to_be_overridden'])
rewrite_options = config_proto.graph_options.rewrite_options
rewrite_options.scoped_allocator_opts.enable_op.append('to_be_removed')

new_config = strategy.update_config_proto(config_proto)

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
