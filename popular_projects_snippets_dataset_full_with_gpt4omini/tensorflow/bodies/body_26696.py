# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/autotune_benchmark.py
batch_size = 16
k = 1024 * 1024
a = (np.random.rand(1, 8 * k), np.random.rand(8 * k, 1))
b = (np.random.rand(1, 4 * k), np.random.rand(4 * k, 1))
c = (np.random.rand(1, 2 * k), np.random.rand(2 * k, 1))
dataset_a = dataset_ops.Dataset.from_tensors(a).repeat()
dataset_b = dataset_ops.Dataset.from_tensors(b).repeat()
dataset_c = dataset_ops.Dataset.from_tensors(c).repeat()

dataset = dataset_a
dataset = dataset.map(
    math_ops.matmul, num_parallel_calls=dataset_ops.AUTOTUNE)
dataset = dataset.batch(batch_size=batch_size)
dataset = dataset_ops.Dataset.range(1).repeat().interleave(
    lambda _: dataset,
    num_parallel_calls=dataset_ops.AUTOTUNE,
    cycle_length=2)

dataset = dataset_ops.Dataset.zip((dataset, dataset_b))
dataset = dataset_ops.Dataset.range(1).repeat().interleave(
    lambda _: dataset,
    num_parallel_calls=dataset_ops.AUTOTUNE,
    cycle_length=2)

dataset_c = dataset_c.map(
    math_ops.matmul, num_parallel_calls=dataset_ops.AUTOTUNE)
dataset_c = dataset_c.batch(batch_size=batch_size)
dataset = dataset_ops.Dataset.zip((dataset, dataset_c))
exit(self._run_benchmark(
    dataset=dataset,
    autotune=autotune,
    benchmark_iters=1000,
    benchmark_label="map_and_batch_and_interleave",
    benchmark_id=benchmark_id))
