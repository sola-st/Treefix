# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/concat_benchmark.py
"""Run the graph and print its execution time.

    Args:
      device: string, the device to run on.
      input_shape: shape of the input tensors.
      variable: whether or not the input shape should be fixed
      num_inputs: the number of inputs to concat
      axis: axis to be concat'ed
      grad: if True compute the gradient
      num_iters: number of steps to run.

    Returns:
      The duration of the run in seconds.
    """
graph = ops.Graph()
with graph.as_default():
    outputs = build_graph(device, input_shape, variable, num_inputs, axis,
                          grad)
config = config_pb2.ConfigProto(graph_options=config_pb2.GraphOptions(
    optimizer_options=config_pb2.OptimizerOptions(
        opt_level=config_pb2.OptimizerOptions.L0)))
with session_lib.Session(graph=graph, config=config) as session:
    variables.global_variables_initializer().run()
    _ = session.run(outputs)  # warm up.
    start_time = time.time()
    for _ in range(num_iters):
        _ = session.run(outputs)
    duration = time.time() - start_time
    print("%s shape:%d/%d var: %r #inputs:%d axis:%d grad:%r - %f secs - %f "
          "GB/sec" % (device, input_shape[0], input_shape[1], variable,
                      num_inputs, axis, grad, duration / num_iters,
                      num_inputs * input_shape[0] * input_shape[1] * 4 * 2 *
                      100 / (duration / num_iters) / 1e9))

name_template = (
    "concat_bench_{device}_input_shape_{shape}_variable_{variable}"
    "_num_inputs_{num_inputs}_axis_{axis}_grad_{grad}")

self.report_benchmark(name=name_template.format(
    device=device,
    num_inputs=num_inputs,
    variable=variable,
    grad=grad,
    shape=str(input_shape).replace(" ", ""),
    axis=str(axis),
    iters=num_iters))

exit(duration)
