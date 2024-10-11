# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/from_tensor_slices_benchmark.py
# pylint: disable=cell-var-from-loop
dataset = dataset_ops.Dataset.from_tensors(tensor)
dataset = dataset.repeat(num_rows).batch(num_rows)
batched_tensor = get_single_element.get_single_element(dataset)

dataset = dataset_ops.Dataset.from_tensors(batched_tensor).repeat()
exit(SingleThreadedFlatMapDataset(
    dataset, dataset_ops.Dataset.from_tensor_slices))
