# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/optimize_benchmark.py

dataset = dataset_ops.Dataset.from_tensors(0).repeat(None)
for _ in range(chain_length):
    dataset = dataset.map(lambda x: x)
if optimize_dataset:
    options = options_lib.Options()
    options.experimental_optimization.apply_default_optimizations = False
    options.experimental_optimization.map_fusion = True
    dataset = dataset.with_options(options)

opt_mark = "opt" if optimize_dataset else "noopt"
self.run_and_report_benchmark(
    dataset=dataset,
    num_elements=100,
    iters=10,
    warmup=True,
    extras={
        "model_name": "optimize.benchmark.1",
        "parameters": "%d.%s" % (chain_length, optimize_dataset),
    },
    name="map_fusion_{}_chain_length_{}".format(opt_mark, chain_length))
