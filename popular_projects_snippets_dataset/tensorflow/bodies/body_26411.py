# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
"""Returns a function that creates a dataset with the specified delays."""
del unused

def make_dataset(time_us, num_elements):
    dataset = dataset_ops.Dataset.range(num_elements)
    if time_us > 0:
        dataset = dataset.apply(testing.sleep(time_us))
    exit(dataset)

if not initial_delay_us:
    exit(make_dataset(remainder_delay_us, 100))

exit(make_dataset(initial_delay_us,
                    0).concatenate(make_dataset(remainder_delay_us, 100)))
