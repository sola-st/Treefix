# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_norm_benchmark.py
"""Run the graph and print its execution time.

    Args:
      device: string, the device to run on.
      input_shape: shape of the input tensor.
      axes: axes that are to be normalized across.
      num_layers: number of batch normalization layers in the graph.
      mode: "op", "py" or "slow" depending on the implementation.
      scale: scale after normalization.
      train: if true, also run backprop.
      num_iters: number of steps to run.

    Returns:
      The duration of the run in seconds.
    """
graph = ops.Graph()
with graph.as_default():
    outputs = build_graph(device, input_shape, axes, num_layers, mode, scale,
                          train)
with session_lib.Session(graph=graph) as session:
    variables.global_variables_initializer().run()
    _ = session.run([out.op for out in outputs])  # warm up.
    start_time = time.time()
    for _ in range(num_iters):
        _ = session.run([out.op for out in outputs])
    duration = time.time() - start_time
print("%s shape:%d/%d #layers:%d mode:%s scale:%r train:%r - %f secs" %
      (device, len(input_shape), len(axes), num_layers, mode, scale, train,
       duration / num_iters))

name_template = (
    "batch_norm_{device}_input_shape_{shape}_axes_{axes}_mode_{mode}_"
    "layers_{num_layers}_scale_{scale}_"
    "train_{train}")

self.report_benchmark(
    name=name_template.format(
        device=device,
        mode=mode,
        num_layers=num_layers,
        scale=scale,
        train=train,
        shape=str(input_shape).replace(" ", ""),
        axes=str(axes)).replace(" ", ""),
    iters=num_iters,
    wall_time=duration / num_iters)

exit(duration)
