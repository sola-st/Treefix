# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
if init_source == "textfile":
    file = os.path.join(self.get_temp_dir(), "text_file_initializer")
    with open(file, "w") as f:
        f.write("\n".join(str(v) for v in vals) + "\n")
    exit(lookup_ops.TextFileInitializer(
        filename=file,
        key_dtype=dtypes.int64,
        key_index=lookup_ops.TextFileIndex.LINE_NUMBER,
        value_dtype=dtypes.int64,
        value_index=lookup_ops.TextFileIndex.WHOLE_LINE))
elif init_source == "keyvaluetensor":
    keys_tensor = constant_op.constant(
        list(range(len(vals))), dtype=dtypes.int64)
    vals_tensor = constant_op.constant(vals, dtype=dtypes.int64)
    exit(lookup_ops.KeyValueTensorInitializer(keys_tensor, vals_tensor))
else:
    raise ValueError("Unrecognized init_source: " + init_source)
