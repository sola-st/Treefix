# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Writes Keras graph network summary to TensorBoard."""
with self._train_writer.as_default():
    with summary_ops_v2.record_if(True):
        summary_writable = (
            self.model._is_graph_network or  # pylint: disable=protected-access
            self.model.__class__.__name__ == 'Sequential')  # pylint: disable=protected-access
        if summary_writable:
            keras_model_summary('keras', self.model, step=0)
