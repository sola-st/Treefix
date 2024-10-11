# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/split_benchmark.py
"""Run the graph and print its execution time.

    Args:
      device: string, the device to run on.
      output_shape: shape of each output tensors.
      variable: whether or not the output shape should be fixed
      num_outputs: the number of outputs to split the input into
      axis: axis to be split

    Returns:
      The duration of the run in seconds.
    """
graph = ops.Graph()
with graph.as_default():
    if not variable:
        if axis == 0:
            input_shape = [output_shape[0] * num_outputs, output_shape[1]]
            sizes = [output_shape[0] for _ in range(num_outputs)]
        else:
            input_shape = [output_shape[0], output_shape[1] * num_outputs]
            sizes = [output_shape[1] for _ in range(num_outputs)]
    else:
        sizes = np.random.randint(
            low=max(1, output_shape[axis] - 2),
            high=output_shape[axis] + 2,
            size=num_outputs)
        total_size = np.sum(sizes)
        if axis == 0:
            input_shape = [total_size, output_shape[1]]
        else:
            input_shape = [output_shape[0], total_size]

    outputs = build_graph(device, input_shape, sizes, axis)
config = config_pb2.ConfigProto(graph_options=config_pb2.GraphOptions(
    optimizer_options=config_pb2.OptimizerOptions(
        opt_level=config_pb2.OptimizerOptions.L0)))
with session_lib.Session(graph=graph, config=config) as session:
    logging.set_verbosity("info")
    variables.global_variables_initializer().run()
    bench = benchmark.TensorFlowBenchmark()
    bench.run_op_benchmark(
        session,
        outputs,
        mbs=input_shape[0] * input_shape[1] * 4 * 2 * 100 / 1e6,
        extras={
            "input_shape": input_shape,
            "variable": variable,
            "axis": axis
        })
