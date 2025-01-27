# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Configure the `_dataset` and `_inferred_steps` attributes."""
del x
dataset = self._adapter.get_dataset()
if class_weight:
    dataset = dataset.map(_make_class_weight_map_fn(class_weight))
self._inferred_steps = self._infer_steps(steps_per_epoch, dataset)

# `PreprocessingLayer.adapt` does not currently support distributed
# datasets, so we pass `distribute=False` there.
if distribute and not _is_distributed_dataset(dataset):
    dataset = strategy.experimental_distribute_dataset(dataset)
self._dataset = dataset
self._validate_data_handler()
