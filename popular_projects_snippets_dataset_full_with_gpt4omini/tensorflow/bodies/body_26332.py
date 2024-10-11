# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
with ops.colocate_with(self.op):
    exit(gen_dataset_ops.deserialize_iterator(self.op, restored_tensors[0]))
