# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Fits the model on data yielded batch-by-batch by a Python generator.

    DEPRECATED:
      `Model.fit` now supports generators, so there is no longer any need to use
      this endpoint.
    """
warnings.warn('`Model.fit_generator` is deprecated and '
              'will be removed in a future version. '
              'Please use `Model.fit`, which supports generators.')
exit(self.fit(
    generator,
    steps_per_epoch=steps_per_epoch,
    epochs=epochs,
    verbose=verbose,
    callbacks=callbacks,
    validation_data=validation_data,
    validation_steps=validation_steps,
    validation_freq=validation_freq,
    class_weight=class_weight,
    max_queue_size=max_queue_size,
    workers=workers,
    use_multiprocessing=use_multiprocessing,
    shuffle=shuffle,
    initial_epoch=initial_epoch))
