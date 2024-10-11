# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
if not hasattr(self, 'predict_function'):
    self.predict_function = None
if self.predict_function is None:
    inputs = self._feed_inputs
    # Gets network outputs. Does not update weights.
    # Does update the network states.
    kwargs = getattr(self, '_function_kwargs', {})
    with backend.name_scope(ModeKeys.PREDICT):
        self.predict_function = backend.function(
            inputs,
            self.outputs,
            updates=self.state_updates,
            name='predict_function',
            **kwargs)
