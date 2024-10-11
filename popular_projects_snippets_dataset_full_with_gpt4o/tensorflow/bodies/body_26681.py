# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/map_and_batch_benchmark.py
"""Compares the performance of chaining and fusing map and batch.

    NOTE: It is recommended to build the benchmark with
    `-c opt --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-gmlt`
    and execute it on a machine with at least 32 CPU cores.
    """

# Sequential pipeline configurations.
seq_elem_size_series = itertools.product([1], [1], [1, 2, 4, 8], [16],
                                         [None], [False, True])
seq_batch_size_series = itertools.product([1], [1], [1], [8, 16, 32, 64],
                                          [None], [False, True])

# Parallel pipeline configuration.
par_elem_size_series = itertools.product([32], [32], [1, 2, 4, 8], [256],
                                         [None], [False, True])
par_batch_size_series = itertools.product([32], [32], [1],
                                          [128, 256, 512, 1024], [None],
                                          [False, True])
par_map_num_calls_series = itertools.product([8, 16, 32, 64], [32], [1],
                                             [512], [None], [False, True])
par_inter_op_series = itertools.product([32], [8, 16, 32, 64], [1], [512],
                                        [None], [False, True])

# Autotuned pipeline configuration.
fused_versus_chained_series = [
    (dataset_ops.AUTOTUNE, 32, 1, 16, dataset_ops.AUTOTUNE, False),
    (dataset_ops.AUTOTUNE, 32, 1, 16, None, True)
]

np.random.seed(_NUMPY_RANDOM_SEED)
self._benchmark_series(
    "Sequential element size evaluation",
    seq_elem_size_series,
    benchmark_id=2)
self._benchmark_series(
    "Sequential batch size evaluation",
    seq_batch_size_series,
    benchmark_id=3)
self._benchmark_series(
    "Parallel element size evaluation",
    par_elem_size_series,
    benchmark_id=4)
self._benchmark_series(
    "Parallel batch size evaluation", par_batch_size_series, benchmark_id=5)
self._benchmark_series(
    "Transformation parallelism evaluation",
    par_map_num_calls_series,
    benchmark_id=6)
self._benchmark_series(
    "Threadpool size evaluation", par_inter_op_series, benchmark_id=7)
self._benchmark_series(
    "Autotune chained versus fused evaluation",
    fused_versus_chained_series,
    benchmark_id=8)
