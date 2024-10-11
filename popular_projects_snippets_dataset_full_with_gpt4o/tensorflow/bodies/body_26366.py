# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/range_benchmark.py
options = options_lib.Options()
options.autotune.enabled = autotune
dataset = dataset_ops.Dataset.range(num_elements)
dataset = dataset.with_options(options)

self.run_and_report_benchmark(
    dataset,
    num_elements=num_elements,
    extras={
        "model_name": "range.benchmark.%d" % benchmark_id,
        "parameters": "%d.%s" % (num_elements, autotune),
    },
    name="modeling_%s" % ("on" if autotune else "off"))
