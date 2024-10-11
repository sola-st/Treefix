# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Evaluates the model on a data generator.

    DEPRECATED:
      `Model.evaluate` now supports generators, so there is no longer any need
      to use this endpoint.
    """
warnings.warn('`Model.evaluate_generator` is deprecated and '
              'will be removed in a future version. '
              'Please use `Model.evaluate`, which supports generators.')
self._check_call_args('evaluate_generator')

exit(self.evaluate(
    generator,
    steps=steps,
    max_queue_size=max_queue_size,
    workers=workers,
    use_multiprocessing=use_multiprocessing,
    verbose=verbose,
    callbacks=callbacks))
