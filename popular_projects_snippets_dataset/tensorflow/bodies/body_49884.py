# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
"""Sets file writer."""
if context.executing_eagerly():
    self.writer = summary_ops_v2.create_file_writer_v2(self.log_dir)
    if not model.run_eagerly and self.write_graph:
        with self.writer.as_default():
            summary_ops_v2.graph(K.get_graph())
elif self.write_graph:
    self.writer = tf_summary.FileWriter(self.log_dir, K.get_graph())
else:
    self.writer = tf_summary.FileWriter(self.log_dir)
