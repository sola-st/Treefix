# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/from_tensor_slices_benchmark.py
non_zeros_per_row_values = [0, 1, 5, 10, 100]
num_rows_values = [32, 64, 128, 1024]

for non_zeros_per_row in non_zeros_per_row_values:
    tensor = sparse_tensor.SparseTensor(
        indices=np.arange(non_zeros_per_row, dtype=np.int64)[:, np.newaxis],
        values=np.arange(non_zeros_per_row, dtype=np.int64),
        dense_shape=[1000])

    for num_rows in num_rows_values:

        # TODO(b/147153744): Function-valued attributes with their own
        # attributes are currently only supported in graph mode.
        @def_function.function
        def make_dataset():
            # pylint: disable=cell-var-from-loop
            dataset = dataset_ops.Dataset.from_tensors(tensor)
            dataset = dataset.repeat(num_rows).batch(num_rows)
            batched_tensor = get_single_element.get_single_element(dataset)

            dataset = dataset_ops.Dataset.from_tensors(batched_tensor).repeat()
            exit(SingleThreadedFlatMapDataset(
                dataset, dataset_ops.Dataset.from_tensor_slices))

        self.run_and_report_benchmark(
            make_dataset(),
            num_elements=100000,
            iters=5,
            extras={
                "model_name": "from_tensor_slices.benchmark.3",
                "parameters": "%d.%d" % (non_zeros_per_row, num_rows),
            },
            name="slice_repeat_sparse_elements_per_row_%d_num_rows_%d" %
            (non_zeros_per_row, num_rows))
