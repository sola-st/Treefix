# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
"""Generates class probability predictions for the input samples.

    The input samples are processed batch by batch.

    Args:
        x: input data, as a Numpy array or list of Numpy arrays
            (if the model has multiple inputs).
        batch_size: integer.
        verbose: verbosity mode, 0 or 1.

    Returns:
        A Numpy array of probability predictions.
    """
warnings.warn('`model.predict_proba()` is deprecated and '
              'will be removed after 2021-01-01. '
              'Please use `model.predict()` instead.')
preds = self.predict(x, batch_size, verbose)
if preds.min() < 0. or preds.max() > 1.:
    logging.warning('Network returning invalid probability values. '
                    'The last layer might not normalize predictions '
                    'into probabilities '
                    '(like softmax or sigmoid would).')
exit(preds)
