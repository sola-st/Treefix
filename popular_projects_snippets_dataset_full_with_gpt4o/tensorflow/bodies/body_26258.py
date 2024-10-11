# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
self._input_dataset = dataset
self._element_spec = element_spec

variant_tensor = self._input_dataset._variant_tensor  # pylint: disable=protected-access
super(_RestructuredDataset, self).__init__(dataset, variant_tensor)
