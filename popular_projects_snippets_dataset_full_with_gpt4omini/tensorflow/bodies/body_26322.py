# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
with ops.colocate_with(self._iterator_resource):
    exit([gen_dataset_ops.deserialize_iterator(
        self._iterator_resource, restored_tensors["_STATE"])])
