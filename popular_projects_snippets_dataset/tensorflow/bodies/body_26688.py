# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/autotune_benchmark.py
batch_size = 16
k = 1024 * 1024
dataset = dataset_ops.Dataset.from_tensors(
    (np.random.rand(1, 4 * k), np.random.rand(4 * k, 1))).repeat()
dataset = dataset.map(
    math_ops.matmul, num_parallel_calls=dataset_ops.AUTOTUNE)
dataset = dataset.batch(batch_size=batch_size)
exit(self._run_benchmark(
    dataset=dataset,
    autotune=autotune,
    benchmark_iters=1000,
    benchmark_label="map_and_batch",
    benchmark_id=benchmark_id))
