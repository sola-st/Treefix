# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
"""Returns a dataset that emulates a remote storage data source.

  Returns a dataset factory which creates a dataset with 100 elements that
  emulates the performance characteristic of a file-based dataset stored in a
  remote storage. In particular, the first element will take an order of
  magnitude longer to produce than the remaining elements (100ms vs. 1ms).

  Args:
    initial_delay_us: How long to wait before producing the first element.
    remainder_delay_us: How long to wait before producing subsequent elements.
  """

def fake_dataset_fn(unused):
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

exit(fake_dataset_fn)
