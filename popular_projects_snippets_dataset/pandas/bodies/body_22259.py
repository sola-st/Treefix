# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    Transform label or iterable of labels to array, for use in Index.

    Parameters
    ----------
    dtype : dtype
        If specified, use as dtype of the resulting array, otherwise infer.

    Returns
    -------
    array
    """
if isinstance(labels, (str, tuple)):
    labels = [labels]

if not isinstance(labels, (list, np.ndarray)):
    try:
        labels = list(labels)
    except TypeError:  # non-iterable
        labels = [labels]

labels = asarray_tuplesafe(labels, dtype=dtype)

exit(labels)
