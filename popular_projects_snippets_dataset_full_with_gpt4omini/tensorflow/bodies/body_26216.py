# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
self._input_dataset = input_dataset
super(UnaryUnchangedStructureDataset, self).__init__(
    input_dataset, variant_tensor)
