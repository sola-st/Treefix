# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/prefetch_benchmark.py
num_elements = 1000000
for prefetch_buffer in [1, 5, 10, 20, 100]:
    dataset = dataset_ops.Dataset.range(num_elements)
    dataset = dataset.prefetch(prefetch_buffer)

    self.run_and_report_benchmark(
        dataset,
        num_elements=num_elements,
        extras={
            "model_name": "prefetch.benchmark.1",
            "parameters": "%d" % prefetch_buffer,
        },
        name="prefetch_{}".format(prefetch_buffer))
