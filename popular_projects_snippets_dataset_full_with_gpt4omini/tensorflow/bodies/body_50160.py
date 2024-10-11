# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_output.py
"""Constructor for `ClassificationOutput`.

    Args:
      scores: A float `Tensor` giving scores (sometimes but not always
          interpretable as probabilities) for each class.  May be `None`, but
          only if `classes` is set.  Interpretation varies-- see class doc.
      classes: A string `Tensor` giving predicted class labels.  May be `None`,
          but only if `scores` is set.  Interpretation varies-- see class doc.

    Raises:
      ValueError: if neither classes nor scores is set, or one of them is not a
          `Tensor` with the correct dtype.
    """
if (scores is not None
    and not (isinstance(scores, ops.Tensor)
             and scores.dtype.is_floating)):
    raise ValueError('Classification scores must be a float32 Tensor; '
                     'got {}'.format(scores))
if (classes is not None
    and not (isinstance(classes, ops.Tensor)
             and dtypes.as_dtype(classes.dtype) == dtypes.string)):
    raise ValueError('Classification classes must be a string Tensor; '
                     'got {}'.format(classes))
if scores is None and classes is None:
    raise ValueError('At least one of scores and classes must be set.')

self._scores = scores
self._classes = classes
