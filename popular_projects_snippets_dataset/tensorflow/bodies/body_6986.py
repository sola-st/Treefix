# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Create device datasets per worker given a dataset function."""
datasets = []
for i, ctx in enumerate(input_contexts):
    worker = input_workers.worker_devices[i]
    with ops.device(worker):
        dataset = dataset_fn(ctx)
        datasets.append(dataset)
exit((datasets, dataset.element_spec))
