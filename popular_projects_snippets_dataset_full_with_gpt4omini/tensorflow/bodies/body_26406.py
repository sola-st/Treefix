# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/filter_benchmark.py
num_elements = 100000
dataset = dataset_ops.Dataset.from_tensors(True)
dataset = dataset.repeat().filter(predicate)
self.run_and_report_benchmark(
    dataset,
    num_elements=num_elements,
    extras={
        "model_name": "filter.benchmark.%d" % benchmark_id,
        "parameters": "%d" % num_elements,
    },
    name=name)
