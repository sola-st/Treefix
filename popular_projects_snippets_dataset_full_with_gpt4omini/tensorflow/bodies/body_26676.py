# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/map_and_batch_benchmark.py
"""Measures the performance of parallelized batching."""
shapes = [(), (10,), (10, 10), (10, 10, 10), (224, 224, 3)]
batch_size_values = [1, 32, 64, 128, 1024]

for shape in shapes:
    for batch_size in batch_size_values:

        dataset = dataset_ops.Dataset.range(1000000000)
        dense_value = random_ops.random_normal(shape=shape)

        dataset = dataset.apply(
            batching.map_and_batch(lambda _: dense_value, batch_size))  # pylint: disable=cell-var-from-loop
        options = options_lib.Options()
        options.experimental_optimization.apply_default_optimizations = False
        dataset = dataset.with_options(options)

        self.run_and_report_benchmark(
            dataset=dataset,
            num_elements=batch_size,
            iters=100,
            warmup=True,
            extras={
                "model_name": "map_and_batch.benchmark.1",
                "parameters": "%d.%s" % (batch_size, str(shape))
            },
            name="num_elements_%d_batch_size_%d" % (np.prod(shape), batch_size))
