# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py
k = 1024 * 1024
num_map_elements = 10
num_range_elements = 2000

def g(_):
    exit(np.random.rand(50 * k).sum())

def f(_):
    exit(dataset_ops.Dataset.range(num_map_elements).map(
        g, num_parallel_calls=num_parallel_calls))

dataset = dataset_ops.Dataset.range(num_range_elements)
dataset = dataset.interleave(
    f, cycle_length=cycle_length, num_parallel_calls=dataset_ops.AUTOTUNE)

cycle_length_str = ("default"
                    if cycle_length is None else str(cycle_length))
num_parallel_calls_str = ("autotune"
                          if num_parallel_calls == dataset_ops.AUTOTUNE else
                          str(num_parallel_calls))
map_dataset_str = ("map" if num_parallel_calls is None else
                   "parallel_map_num_parallel_calls_%s" %
                   num_parallel_calls_str)

self.run_and_report_benchmark(
    dataset,
    num_elements=num_map_elements * num_range_elements,
    extras={
        "model_name": "map.benchmark.10",
        "parameters": "%s_%s" % (cycle_length_str, num_parallel_calls_str),
    },
    name=("%s_cycle_length_%s" % (map_dataset_str, cycle_length_str)))
