# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/autotune_benchmark.py
k = 1024 * 1024
dataset = dataset_ops.Dataset.from_tensors(
    (np.random.rand(1, 4 * k), np.random.rand(4 * k, 1))).repeat()
dataset = dataset.map(math_ops.matmul)
dataset = dataset_ops.Dataset.range(1).repeat().interleave(
    lambda _: dataset,
    cycle_length=10,
    num_parallel_calls=dataset_ops.AUTOTUNE)
exit(self._run_benchmark(
    dataset=dataset,
    autotune=autotune,
    benchmark_iters=10000,
    benchmark_label="interleave",
    benchmark_id=benchmark_id))
