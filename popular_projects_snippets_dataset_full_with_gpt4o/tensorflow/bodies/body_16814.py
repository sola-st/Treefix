# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
group_size = 2
group_key = 1
instance_key1 = 1
instance_key2 = 2

graph_options = config_pb2.GraphOptions(
    optimizer_options=config_pb2.OptimizerOptions(do_constant_folding=True))
cfg = config_pb2.ConfigProto(device_count={'CPU': group_size},
                             graph_options=graph_options)
rewrite_options = cfg.graph_options.rewrite_options
rewrite_options.scoped_allocator_optimization = (
    rewriter_config_pb2.RewriterConfig.ON)
del rewrite_options.scoped_allocator_opts.enable_op[:]
rewrite_options.scoped_allocator_opts.enable_op.append('CollectiveReduce')

# Tests that execute collectives need to be enclosed in graph or tf.function
with ops.Graph().as_default():
    with self.session(config=cfg) as sess:
        run_ops = []
        for i in range(group_size):
            with ops.device('CPU:%d' % i):
                constant = constant_op.constant(i + 1.)
                input_tensor1 = array_ops.identity(constant)
                input_tensor2 = array_ops.identity(constant)
                reduced_tensor1 = collective_ops.all_reduce(
                    input_tensor1, group_size, group_key, instance_key1, 'Add',
                    'Id')
                reduced_tensor2 = collective_ops.all_reduce(
                    input_tensor2, group_size, group_key, instance_key2, 'Add',
                    'Id')
                run_ops.append(array_ops.identity(reduced_tensor1))
                run_ops.append(array_ops.identity(reduced_tensor2))
        results = sess.run(run_ops)
self.assertEqual(results, [3., 3., 3., 3.])
