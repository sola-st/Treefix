# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
dataset = dataset_ops.Dataset.range(1).repeat()
interleave_fn = _make_fake_dataset_fn(initial_delay, remainder_delay)
exit(self.apply_interleave(
    interleave_version=interleave_version,
    dataset=dataset,
    interleave_fn=interleave_fn,
    cycle_length=cycle_length,
    num_parallel_calls=num_parallel_calls))
