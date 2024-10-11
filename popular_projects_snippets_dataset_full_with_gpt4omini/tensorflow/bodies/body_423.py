# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v0_11.py
with self.cached_session() as s:

    # make some variables
    _ = [tf.Variable([1, 2, 3], dtype=tf.float32),
         tf.Variable([1, 2, 3], dtype=tf.int32)]
    s.run(tf.global_variables_initializer())
    _ = [v.name for v in tf.all_variables()]
    _ = [v.name for v in tf.local_variables()]
