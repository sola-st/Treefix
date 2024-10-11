# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
tensors = table.export()
specs = [
    BaseSaverBuilder.SaveSpec(tensors[0], "", name + "-keys"),
    BaseSaverBuilder.SaveSpec(tensors[1], "", name + "-values")
]
self.table_name = table_name or name
# pylint: disable=protected-access
super(DenseHashTable._Saveable, self).__init__(table, specs, name)
