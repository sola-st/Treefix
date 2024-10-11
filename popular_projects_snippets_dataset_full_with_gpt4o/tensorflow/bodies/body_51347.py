# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
export_graph = ops.Graph()
vocab_path = os.path.join(self.get_temp_dir(), "vocab.txt")
with open(vocab_path, "w") as f:
    f.write("alpha\nbeta\ngamma\n")
with export_graph.as_default():
    initializer = lookup_ops.TextFileInitializer(
        vocab_path,
        key_dtype=dtypes.string,
        key_index=lookup_ops.TextFileIndex.WHOLE_LINE,
        value_dtype=dtypes.int64,
        value_index=lookup_ops.TextFileIndex.LINE_NUMBER)
    table = lookup_ops.HashTable(
        initializer, default_value=-1)
    start = array_ops.placeholder(
        shape=None, dtype=dtypes.string, name="in")
    output = table.lookup(start, name="out")
    if clear_shared_name:
        export_graph.get_operation_by_name("hash_table")._clear_attr(
            "shared_name")
    with session_lib.Session() as session:
        session.run([table.initializer])
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        simple_save.simple_save(
            session,
            path,
            inputs={"start": start},
            outputs={"output": output},
            legacy_init_op=table.initializer)
file_io.delete_file(vocab_path)
exit(path)
