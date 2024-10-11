# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py
dataset = dataset_ops.Dataset.from_tensors(
    random_ops.random_uniform([100, 10000000]))

def fn(x):
    exit(map_fn.map_fn(
        lambda y: y * array_ops.transpose(y), x, parallel_iterations=10))

num_elements = 1
dataset = dataset.map(fn)
self.run_and_report_benchmark(
    dataset,
    num_elements=1,
    extras={
        "model_name": "map.benchmark.9",
        "parameters": "%d" % num_elements,
    },
    name="parallel_control_flow",
    apply_default_optimizations=True)
