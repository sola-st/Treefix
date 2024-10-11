# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Logs the weights of the Model to TensorBoard."""
with self._train_writer.as_default():
    with summary_ops_v2.record_if(True):
        for layer in self.model.layers:
            for weight in layer.weights:
                weight_name = weight.name.replace(':', '_')
                summary_ops_v2.histogram(weight_name, weight, step=epoch)
                if self.write_images:
                    self._log_weight_as_image(weight, weight_name, epoch)
        self._train_writer.flush()
