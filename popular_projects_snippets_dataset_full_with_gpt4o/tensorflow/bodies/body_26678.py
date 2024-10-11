# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/map_and_batch_benchmark.py
k = 1024 * 1024
x = constant_op.constant(np.random.rand(element_size, 4 * k))
y = constant_op.constant(np.random.rand(4 * k, 1))
dataset = dataset_ops.Dataset.range(1000000000000).map(lambda _: (x, y))
dataset = dataset.map(math_ops.matmul, num_parallel_calls=map_num_calls)
dataset = dataset.batch(
    batch_size=batch_size, num_parallel_calls=batch_num_calls)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.map_and_batch_fusion = apply_fusion
dataset = dataset.with_options(options)
exit(dataset)
