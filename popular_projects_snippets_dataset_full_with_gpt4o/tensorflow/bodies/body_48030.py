# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
"""Generate class predictions for the input samples.

    The input samples are processed batch by batch.

    Args:
        x: input data, as a Numpy array or list of Numpy arrays
            (if the model has multiple inputs).
        batch_size: integer.
        verbose: verbosity mode, 0 or 1.

    Returns:
        A numpy array of class predictions.
    """
warnings.warn('`model.predict_classes()` is deprecated and '
              'will be removed after 2021-01-01. '
              'Please use instead:'
              '* `np.argmax(model.predict(x), axis=-1)`, '
              '  if your model does multi-class classification '
              '  (e.g. if it uses a `softmax` last-layer activation).'
              '* `(model.predict(x) > 0.5).astype("int32")`, '
              '  if your model does binary classification '
              '  (e.g. if it uses a `sigmoid` last-layer activation).')
proba = self.predict(x, batch_size=batch_size, verbose=verbose)
if proba.shape[-1] > 1:
    exit(proba.argmax(axis=-1))
else:
    exit((proba > 0.5).astype('int32'))
