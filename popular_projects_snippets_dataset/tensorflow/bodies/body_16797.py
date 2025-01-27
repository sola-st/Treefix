# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
group_size = 2
group_key = 1
instance_key0 = 1
instance_key1 = 2

config = config_pb2.ConfigProto(device_count={'CPU': group_size})
rewrite_options = config.graph_options.rewrite_options
rewrite_options.scoped_allocator_optimization = (
    rewriter_config_pb2.RewriterConfig.ON)
del rewrite_options.scoped_allocator_opts.enable_op[:]
rewrite_options.scoped_allocator_opts.enable_op.append('CollectiveReduce')

# Tests that execute collectives need to be enclosed in graph or tf.function
with ops.Graph().as_default():
    with self.session(config=config) as sess:
        run_ops = []
        for i in range(group_size):
            with ops.device('CPU:%d' % i):
                constant = constant_op.constant(0.)
                cond = lambda i: math_ops.less(i, 10.)
                body = lambda i: math_ops.add(i, 1.)
                input0 = control_flow_ops.while_loop(cond, body, [constant])
                input1 = math_ops.add(constant, 5)
                colred0 = collective_ops.all_reduce(input0, group_size, group_key,
                                                    instance_key0, 'Add', 'Id')
                colred1 = collective_ops.all_reduce(input1, group_size, group_key,
                                                    instance_key1, 'Add', 'Id')
                run_ops.append(math_ops.add_n([colred0, colred1]))
        results = sess.run(run_ops)
    self.assertEqual(results, [30., 30.])
