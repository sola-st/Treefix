# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test.py
"""Build a graph and run benchmarks against it, with or without XLA.

  Args:
    tf_bench: An instance of tf.test.Benchmark, used to run the benchmark.
    builder_fn: A function that builds a graph when invoked, and returns
        (name, fetches), where name is the name of the test, and fetches
        is a list of tensors to fetch as output.
    use_xla_jit: If true compile with the XLA JIT, otherwise use regular TF.
    device: The tensorflow device to run on, e.g. "cpu", "gpu".
    separate_compiled_gradients: If true put each gradient subgraph into a
      separate compilation scope. This gives fine-grained control over which
      portions of the graph will be compiled as a single unit. Compiling
      gradients separately may yield better performance for some graphs.
      The scope is named based on the scope of the forward computation as well
      as the name of the gradients. As a result, the gradients will be compiled
      in a scope that is separate from both the forward computation, and from
      other gradients.
  """

with ops.Graph().as_default():
    name = None
    targets = []
    with ops.device(device):
        fetches = []
        jit_scope = jit.experimental_jit_scope
        with jit_scope(
            compile_ops=use_xla_jit,
            separate_compiled_gradients=separate_compiled_gradients):
            name, fetches = builder_fn()

        # We only want to benchmark the operations themselves, and not the data
        # transfer of the result(s).  Non-compiled identity ops ensure XLA
        # doesn't know we're dropping the results, otherwise it might compile
        # away the entire computation.
        for fetch in fetches:
            targets.append(array_ops.identity(fetch).op)

    # TODO(b/132430685):  Should we allow soft placement here?
    config = config_pb2.ConfigProto(allow_soft_placement=True)
    with session.Session(config=config) as sess:
        sess.run(variables.global_variables_initializer())
        xla = 'xla_' if use_xla_jit else ''
        tf_bench.run_op_benchmark(
            sess, targets, name='%s_%s%s' % (name, xla, device))
