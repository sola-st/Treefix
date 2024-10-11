# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/batch_benchmark.py
for element_exp in [10, 12, 14, 16, 18, 20, 22]:
    for batch_exp in [3, 6, 9]:
        element_size = 1 << element_exp
        batch_size = 1 << batch_exp
        dataset = dataset_ops.Dataset.from_tensors(
            np.random.rand(element_size)).repeat().batch(batch_size)
        options = options_lib.Options()
        options.experimental_optimization.parallel_batch = parallel_copy
        dataset = dataset.with_options(options)
        tag = "_parallel_copy" if parallel_copy else ""
        self.run_and_report_benchmark(
            dataset,
            num_elements=(1 << (22 - ((batch_exp + element_exp) // 2))),
            iters=1,
            extras={
                "model_name": "batch.benchmark.%d" % benchmark_id,
                "parameters": "%d.%d" % (batch_size, element_size),
            },
            name="batch_element_size_%d_batch_size_%d%s" %
            (element_size, batch_size, tag))
