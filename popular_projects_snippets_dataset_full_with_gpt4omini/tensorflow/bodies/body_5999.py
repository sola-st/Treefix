# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
vals = [0, 1, 2]
if init_source == "textfile":

    with open(filepath, "w") as f:
        f.write("\n".join(str(v) for v in vals) + "\n")

    self.initializer = lookup_ops.TextFileInitializer(
        filepath, dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER,
        dtypes.int64, lookup_ops.TextFileIndex.WHOLE_LINE)
else:
    keys_tensor = constant_op.constant(
        list(range(len(vals))), dtype=dtypes.int64)
    vals_tensor = constant_op.constant(vals, dtype=dtypes.int64)
    self.initializer = lookup_ops.KeyValueTensorInitializer(
        keys_tensor, vals_tensor)

self.table = lookup_ops.StaticHashTable(
    self.initializer, default_value=-2)
