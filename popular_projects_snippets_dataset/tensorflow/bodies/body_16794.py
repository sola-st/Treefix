# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
group_size = 2
group_key = 1
instances = [(key_base + i) for i in range(num_vars)]
devices = ['CPU:{}'.format(i) for i in range(group_size)]

config = config_pb2.ConfigProto(device_count={'CPU': group_size})
rewrite_options = config.graph_options.rewrite_options
rewrite_options.scoped_allocator_optimization = (
    rewriter_config_pb2.RewriterConfig.ON)
del rewrite_options.scoped_allocator_opts.enable_op[:]
rewrite_options.scoped_allocator_opts.enable_op.append('CollectiveReduce')

with self.session(config=config) as sess:
    loop_vars = []
    for device in devices:
        with ops.device(device):
            loop_vars.append(
                [variables.VariableV1((1 << i) * 1.) for i in range(num_vars)])
      # This variable controls number of iterations.
    loop_vars.append(variables.VariableV1(0.))
    def loop_body(dev0_tensors, dev1_tensors, loop_tensor):
        return_ops = []
        for i in range(len(devices)):
            device = devices[i]
            device_tensors = dev0_tensors if i == 0 else dev1_tensors
            with ops.device(device):
                device_collectives = []
                for j in range(num_vars):
                    # NOTE(ayushd): we need the `cast` here to ensure that the input
                    # to `all_reduce` has an explicit device string.  We don't use
                    # `identity` because `cast` is more resilient to getting optimized
                    # away by various optimization passes.
                    input_tensor = math_ops.cast(device_tensors[j], dtypes.float16)
                    collective_op = collective_ops.all_reduce(
                        input_tensor, group_size, group_key, instances[j],
                        'Add', 'Id')
                    output_tensor = math_ops.cast(collective_op, dtypes.float32)
                    device_collectives.append(output_tensor)
                return_ops.append(device_collectives)
        return_ops.append(math_ops.add(loop_tensor, 1.))
        exit(return_ops)
    # Run until last variable exceeds number of iterations.
    loop_cond = lambda d0, d1, i: math_ops.less(i, num_iterations)
    sess.run(variables.global_variables_initializer())
    results = sess.run(control_flow_ops.while_loop(loop_cond, loop_body,
                                                   loop_vars))
    self.assertEqual(results[:-1], [
        [((1 << (num_iterations + v)) * 1.) for v in range(num_vars)]
        for _ in range(group_size)])
