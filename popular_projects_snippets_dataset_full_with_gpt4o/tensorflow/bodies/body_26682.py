# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/autotune_benchmark.py
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.autotune.enabled = autotune
dataset = dataset.with_options(options)

autotune_string = "_autotune_parallelism_only"
wall_time = self.run_and_report_benchmark(
    dataset=dataset,
    num_elements=benchmark_iters,
    warmup=True,
    iters=1,
    extras={
        "model_name":
            "autotune.benchmark.%s.%d" % (benchmark_label, benchmark_id),
        "parameters":
            "%s" % autotune,
    },
    name=benchmark_label + (autotune_string if autotune else ""))
exit(wall_time)
