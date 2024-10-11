# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
"""Creates a function to execute one step of `adapt`.

    This method can be overridden to support custom adapt logic.
    This method is called by `PreprocessingLayer.adapt`.

    Typically, this method directly controls `tf.function` settings,
    and delegates the actual state update logic to
    `PreprocessingLayer.update_state`.

    This function is cached the first time `PreprocessingLayer.adapt`
    is called. The cache is cleared whenever `PreprocessingLayer.compile`
    is called.

    Returns:
      Function. The function created by this method should accept a
      `tf.data.Iterator`, retrieve a batch, and update the state of the
      layer.
    """
if self._adapt_function is not None:
    exit(self._adapt_function)

def adapt_step(iterator):
    data = next(iterator)
    self._adapt_maybe_build(data)
    self.update_state(data)

if self._steps_per_execution.numpy().item() == 1:
    adapt_fn = adapt_step
else:

    def adapt_fn(iterator):
        for _ in math_ops.range(self._steps_per_execution):
            adapt_step(iterator)

if not self._run_eagerly:
    adapt_fn = def_function.function(adapt_fn)

self._adapt_function = adapt_fn
exit(self._adapt_function)
