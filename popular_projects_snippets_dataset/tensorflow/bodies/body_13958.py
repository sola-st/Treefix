# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
for size in sizes:
    for ninput in ninputs:
        graph = ops.Graph()
        with graph.as_default():
            inputs = input_fn(size, ninput)

        format_args = (tag, size, ninput, repeats)
        self._SetupAndRunBenchmark(graph, inputs, repeats, format_args)
