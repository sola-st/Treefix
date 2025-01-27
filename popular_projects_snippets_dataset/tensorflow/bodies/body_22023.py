# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
x = variable_scope.get_variable(
    "x",
    shape=[4, 1],
    initializer=ones(),
    partitioner=lambda shape, dtype: [2, 1])

# List of PartitionedVariable is invalid type when warm-starting with vocab.
self.assertRaises(TypeError, ws_util._warm_start_var_with_vocab, [x],
                  "/tmp", 5, "/tmp", "/tmp")

# Unused variable names raises ValueError.
with ops.Graph().as_default():
    with self.cached_session() as sess:
        x = variable_scope.get_variable(
            "x",
            shape=[4, 1],
            initializer=ones(),
            partitioner=lambda shape, dtype: [2, 1])
        self._write_checkpoint(sess)

self.assertRaises(
    ValueError,
    ws_util.warm_start,
    self.get_temp_dir(),
    var_name_to_vocab_info={"y": ws_util.VocabInfo("", 1, 0, "")})
self.assertRaises(
    ValueError,
    ws_util.warm_start,
    self.get_temp_dir(),
    var_name_to_prev_var_name={"y": "y2"})
