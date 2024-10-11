# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
if interleave_version == NON_PARALLEL:
    exit(dataset.interleave(interleave_fn, cycle_length=cycle_length))
elif interleave_version == EXPERIMENTAL_PARALLEL:
    exit(dataset.apply(
        interleave_ops.parallel_interleave(
            interleave_fn, cycle_length=cycle_length)))
elif interleave_version == CORE_PARALLEL:
    if not num_parallel_calls:
        num_parallel_calls = cycle_length
    exit(dataset.interleave(
        interleave_fn,
        cycle_length=cycle_length,
        num_parallel_calls=num_parallel_calls))
else:
    raise ValueError("Unknown version: " + interleave_version)
