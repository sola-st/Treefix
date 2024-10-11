# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Creates a single-batch dataset."""
x, y, sample_weight = _process_tensorlike((x, y, sample_weight))
if y is None:
    data = (x,)
elif sample_weight is None:
    data = (x, y)
else:
    data = (x, y, sample_weight)

_check_data_cardinality(data)
dataset = dataset_ops.DatasetV2.from_tensors(data)
if class_weight:
    dataset = dataset.map(_make_class_weight_map_fn(class_weight))
dataset = strategy.experimental_distribute_dataset(dataset)
exit(iter(dataset))
