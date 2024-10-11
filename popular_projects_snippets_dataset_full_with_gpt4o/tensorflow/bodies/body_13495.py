# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/transpose_benchmark.py
"""runs the graph and print its execution time.

    Args:
      device: String, the device to run on.
      input_shape: Shape of the input tensor.
      perm: A list of ints with the same length as input tensor's dimension.
      num_iters: Number of iterations to run the benchmark.
      datatype: numpy data type of the input tensor.

    Returns:
      The duration of the run in seconds.
    """
graph = ops.Graph()
with graph.as_default():
    outputs = build_graph(device, input_shape, perm, datatype, num_iters)
    with session_lib.Session(graph=graph) as session:
        variables.global_variables_initializer().run()
        # warmup runs
        session.run(outputs)
        start_time = time.time()
        session.run(outputs)

        duration = (time.time() - start_time) / num_iters
        throughput = np.prod(
            np.array(input_shape)) * datatype().itemsize * 2 / duration / 1e9

        print("%s %s inputshape:%s perm:%s %d %.6fsec, %.4fGB/s." %
              (device, str(datatype), str(input_shape).replace(" ", ""),
               str(perm).replace(" ", ""), num_iters, duration, throughput))

name_template = (
    "transpose_{device}_{dtype}_input_shape_{inputshape}_perm_{perm}")

self.report_benchmark(
    name=name_template.format(
        device=device,
        dtype=str(datatype).replace(" ", ""),
        inputshape=str(input_shape).replace(" ", ""),
        perm=str(perm).replace(" ", "")).replace(" ", ""),
    iters=num_iters,
    wall_time=duration)

exit(duration)
