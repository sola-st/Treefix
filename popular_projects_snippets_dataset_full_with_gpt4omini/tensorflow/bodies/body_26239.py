# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
exit(DatasetSpec(
    self._element_spec,
    tensor_shape.TensorShape([batch_size]).concatenate(self._dataset_shape)))
