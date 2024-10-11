# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if self.model.optimizer and hasattr(self.model.optimizer, 'iterations'):
    with summary_ops_v2.record_if(True), self._val_writer.as_default():
        for name, value in logs.items():
            summary_ops_v2.scalar(
                'evaluation_' + name + '_vs_iterations',
                value,
                step=self.model.optimizer.iterations.read_value())
self._pop_writer()
