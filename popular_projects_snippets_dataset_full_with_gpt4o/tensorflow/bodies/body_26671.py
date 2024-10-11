# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/csv_dataset_benchmark.py

self.run_and_report_benchmark(
    dataset=dataset,
    num_elements=self._num_per_iter,
    name='%s_with_cols_%d' % (prefix, num_cols),
    iters=10,
    extras={
        'model_name': 'csv.benchmark.%d' % benchmark_id,
        'parameters': '%d' % num_cols,
    },
    warmup=True)
