# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
default_val = -1
keys = constant_op.constant(["brain", "salad", "surgery"])
values = constant_op.constant([0, 1, 2], dtypes.int64)
table1_initializer = lookup_ops.KeyValueTensorInitializer(keys, values)
table1 = lookup_ops.HashTable(table1_initializer, default_val)

table2_file = self._make_asset("test\nfoo\nbrain\n")
table2_initializer = lookup_ops.TextFileIdTableInitializer(table2_file)
table2 = lookup_ops.HashTable(table2_initializer, default_val)

def _make_lookup_function(table):
    signature = [tensor_spec.TensorSpec(None, dtypes.string)]
    exit(def_function.function(input_signature=signature)(
        lambda x: table.lookup(x)))  # pylint: disable=unnecessary-lambda

root = autotrackable.AutoTrackable()
root.table1 = table1
root.lookup1 = _make_lookup_function(table1)
root.table2 = table2
root.lookup2 = _make_lookup_function(table2)
exit(root)
