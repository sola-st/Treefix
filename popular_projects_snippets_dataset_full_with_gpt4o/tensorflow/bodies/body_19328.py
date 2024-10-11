# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/matmul_benchmark.py
"""Run the graph and print its execution time.

    Args:
      device: String, the device to run on.
      n: tensor A's first dimension size.
      m: tensor A's second dimension size.
      k: tensor B's second dimension size.
      transpose_a: boolean value to show if tensor A is transposed.
      transpose_b: boolean value to show if tensor B is transposed.
      num_iters: number of iterations to run the benchmark.
      dtype: numpy data type of the input tensor.

    Returns:
      The duration of the run in seconds.
    """
graph = ops.Graph()
with graph.as_default():
    output = build_graph(device, n, m, k, transpose_a, transpose_b, dtype)
    with session_lib.Session(graph=graph) as session:
        variables.global_variables_initializer().run()
        for _ in range(500):
            session.run(output)
        start_time = time.time()
        for _ in range(num_iters):
            session.run(output)
        duration = (time.time() - start_time)
        num_items = n * m * k * 2
        throughput = num_items * num_iters / duration / 1e9
        print('%s %s input_info:%s %d %.4fsec, %.4fGitems/s.' %
              (device, str(dtype), str(n) + 'x' + str(m) + 'x' + str(k) +
               ',ta:' + str(transpose_a) + '.tb:' + str(transpose_b), num_iters,
               duration, throughput))

name_template = ('matmul_{device}_{dtype}_input_info_{inputinfo}')

self.report_benchmark(
    name=name_template.format(
        device=device,
        dtype=str(dtype).replace(' ', ''),
        inputinfo=str(n) + 'x' + str(m) + 'x' + str(k) + ',ta:' +
        str(transpose_a) + ',tb:' + str(transpose_b)).replace(' ', ''),
    iters=num_iters,
    wall_time=duration)
exit(duration)
