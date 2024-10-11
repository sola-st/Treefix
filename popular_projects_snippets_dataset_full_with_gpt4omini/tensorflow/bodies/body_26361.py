# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/batch_benchmark.py
non_zeros_per_row_values = [0, 1, 5, 10, 100]
batch_size_values = [1, 32, 64, 128, 1024]

for non_zeros_per_row in non_zeros_per_row_values:

    tensor = sparse_tensor.SparseTensor(
        indices=np.arange(non_zeros_per_row, dtype=np.int64)[:, np.newaxis],
        values=np.arange(non_zeros_per_row, dtype=np.int64),
        dense_shape=[1000])

    for batch_size in batch_size_values:
        dataset = dataset_ops.Dataset.from_tensors(tensor).repeat().batch(
            batch_size)
        self.run_and_report_benchmark(
            dataset,
            num_elements=100000 // batch_size,
            iters=1,
            extras={
                "model_name": "batch.benchmark.1",
                "parameters": "%d.%d" % (batch_size, non_zeros_per_row),
            },
            name="sparse_num_elements_%d_batch_size_%d" %
            (non_zeros_per_row, batch_size))
