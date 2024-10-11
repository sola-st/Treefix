# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/conv2d_benchmark.py
"""runs the graph and print its execution time.

    Args:
      device: String, the device to run on.
      dtype: Data type for the convolution.
      data_format: A string from: "NHWC" or "NCHW". Data format for input and
                   output data.
      input_shape: Shape of the input tensor.
      filter_shape: Shape of the filter tensor.
      strides: A list of ints. 1-D of length 4. The stride of sliding
               window for each dimension of input.
      padding: A string from: "SAME", "VALID". The type of padding
               algorithm to use.  num_iters: Number of iterations to run the
                 benchmark.
      num_iters: number of iterations to run conv2d.
      warmup_iters: number of iterations for warmup runs.

    Returns:
      The duration of the run in seconds.
    """
graph = ops.Graph()
with graph.as_default():
    warmup_outputs, outputs = build_graph(device, dtype, data_format,
                                          input_shape, filter_shape, strides,
                                          padding, num_iters, warmup_iters)

    config = config_pb2.ConfigProto()
    config.graph_options.optimizer_options.opt_level = -1
    rewrite_options = config.graph_options.rewrite_options

    # Disable layout optimizer to not change input data_format.
    rewrite_options.layout_optimizer = (
        rewriter_config_pb2.RewriterConfig.ON if FLAGS.enable_layout_optimizer
        else rewriter_config_pb2.RewriterConfig.OFF)
    # Convolution ops are effectively noop in the test graph as we are not
    # fetching the convolution outputs. Disable dependency optimizer to not
    # remove the conv ops.
    rewrite_options.dependency_optimization = (
        rewriter_config_pb2.RewriterConfig.OFF)

    with session_lib.Session(graph=graph, config=config) as session:
        # TODO(hinsu): Use run_op_benchmark method from test.Benchmark to run
        # benchmark along with warmup.
        variables.global_variables_initializer().run()
        # warmup runs
        session.run(warmup_outputs)

        start_time = time.time()
        session.run(outputs)
        duration = (time.time() - start_time) / num_iters
        print("%s %s %s inputshape:%s filtershape:%s strides:%s padding:%s "
              "%d iters: %.8f sec" %
              (device, str(dtype), data_format, str(input_shape).replace(
                  " ", ""), str(filter_shape).replace(" ", ""),
               str(strides).replace(" ", ""), padding, num_iters, duration))

name_template = (
    "conv2d_{device}_{datatype}_{data_format}_input_shape_{inputshape}_"
    "filter_shape_{filtershape}_strides_{strides}_padding_{padding}")

self.report_benchmark(
    name=name_template.format(
        device=device,
        datatype=str(dtype),
        data_format=str(data_format),
        inputshape=str(input_shape).replace(" ", ""),
        filtershape=str(filter_shape).replace(" ", ""),
        strides=str(strides).replace(" ", ""),
        padding=padding).replace(" ", ""),
    iters=num_iters,
    wall_time=duration)

exit(duration)
