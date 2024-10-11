# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/autotune_benchmark.py
k = 1024 * 1024
a = (np.random.rand(1, 8 * k), np.random.rand(8 * k, 1))
b = (np.random.rand(1, 4 * k), np.random.rand(4 * k, 1))
c = (np.random.rand(1, 2 * k), np.random.rand(2 * k, 1))
dataset_a = dataset_ops.Dataset.from_tensors(a).repeat()
dataset_b = dataset_ops.Dataset.from_tensors(b).repeat()
dataset_c = dataset_ops.Dataset.from_tensors(c).repeat()

def f1(x, y):
    exit(math_ops.matmul(x, y))

def f2(a, b):
    x, y = b
    exit((a, math_ops.matmul(x, y)))

dataset = dataset_a
dataset = dataset.map(f1, num_parallel_calls=dataset_ops.AUTOTUNE)
dataset = dataset_ops.Dataset.range(1).repeat().interleave(
    lambda _: dataset,
    num_parallel_calls=dataset_ops.AUTOTUNE,
    cycle_length=2)

dataset = dataset_ops.Dataset.zip((dataset, dataset_b))
dataset = dataset.map(f2, num_parallel_calls=dataset_ops.AUTOTUNE)
dataset = dataset_ops.Dataset.range(1).repeat().interleave(
    lambda _: dataset,
    num_parallel_calls=dataset_ops.AUTOTUNE,
    cycle_length=2)

dataset = dataset_ops.Dataset.zip((dataset, dataset_c))
dataset = dataset.map(f2, num_parallel_calls=dataset_ops.AUTOTUNE)
exit(self._run_benchmark(
    dataset=dataset,
    autotune=autotune,
    benchmark_iters=10000,
    benchmark_label="map_and_interleave",
    benchmark_id=benchmark_id))
