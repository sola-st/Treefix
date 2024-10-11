# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Generates predictions for the input samples from a data generator.

    DEPRECATED:
      `Model.predict` now supports generators, so there is no longer any need
      to use this endpoint.
    """
warnings.warn('`Model.predict_generator` is deprecated and '
              'will be removed in a future version. '
              'Please use `Model.predict`, which supports generators.')
exit(self.predict(
    generator,
    steps=steps,
    max_queue_size=max_queue_size,
    workers=workers,
    use_multiprocessing=use_multiprocessing,
    verbose=verbose,
    callbacks=callbacks))
