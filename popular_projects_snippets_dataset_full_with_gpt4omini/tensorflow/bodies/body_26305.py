# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""The type specification of an element of this iterator.

    >>> dataset = tf.data.Dataset.from_tensors(42)
    >>> iterator = iter(dataset)
    >>> iterator.element_spec
    tf.TensorSpec(shape=(), dtype=tf.int32, name=None)

    For more information,
    read [this guide](https://www.tensorflow.org/guide/data#dataset_structure).

    Returns:
      A (nested) structure of `tf.TypeSpec` objects matching the structure of an
      element of this iterator, specifying the type of individual components.
    """
raise NotImplementedError("Iterator.element_spec")
