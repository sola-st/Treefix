# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Writes Keras model train_function graph to TensorBoard."""
with self._train_writer.as_default():
    with summary_ops_v2.record_if(True):
        train_fn = self.model.train_tf_function
        # If the train_function is a `tf.function`, we can write out a graph
        if hasattr(train_fn, 'function_spec'):
            summary_ops_v2.graph(train_fn._concrete_stateful_fn.graph)  # pylint: disable=protected-access
