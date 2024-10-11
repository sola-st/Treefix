# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/distribute.py
# pylint: disable=protected-access
batch_size = recalculate_batch_size(type_spec)
exit(type_spec._unbatch()._batch(batch_size))
