# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/map_and_batch_benchmark.py
exit(1024 // (
    (element_size * batch_size) //
    min(12 if map_num_calls == dataset_ops.AUTOTUNE else map_num_calls,
        inter_op)))
