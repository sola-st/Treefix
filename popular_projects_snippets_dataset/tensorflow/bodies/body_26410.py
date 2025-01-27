# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
dataset = dataset_ops.Dataset.range(num_elements)
if time_us > 0:
    dataset = dataset.apply(testing.sleep(time_us))
exit(dataset)
