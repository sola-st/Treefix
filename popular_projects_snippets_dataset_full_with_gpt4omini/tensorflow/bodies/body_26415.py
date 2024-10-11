# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
dataset = self.make_dataset(
    interleave_version=interleave_version,
    initial_delay=initial_delay_us,
    remainder_delay=remainder_delay_us,
    cycle_length=cycle_length,
    num_parallel_calls=num_parallel_calls)

self.run_and_report_benchmark(
    dataset=dataset,
    num_elements=num_elements,
    iters=iters,
    warmup=True,
    extras={
        "model_name":
            "interleave.benchmark.%s.%d" % (benchmark_label, benchmark_id),
        "parameters":
            "%d.%d.%d.%s" %
            (num_elements, cycle_length, iters, str(num_parallel_calls)),
    },
    name=name)
