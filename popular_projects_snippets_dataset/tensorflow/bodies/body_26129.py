# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Loads a previously saved dataset.

    Example usage:

    >>> import tempfile
    >>> path = os.path.join(tempfile.gettempdir(), "saved_data")
    >>> # Save a dataset
    >>> dataset = tf.data.Dataset.range(2)
    >>> tf.data.Dataset.save(dataset, path)
    >>> new_dataset = tf.data.Dataset.load(path)
    >>> for elem in new_dataset:
    ...   print(elem)
    tf.Tensor(0, shape=(), dtype=int64)
    tf.Tensor(1, shape=(), dtype=int64)


    If the default option of sharding the saved dataset was used, the element
    order of the saved dataset will be preserved when loading it.

    The `reader_func` argument can be used to specify a custom order in which
    elements should be loaded from the individual shards. The `reader_func` is
    expected to take a single argument -- a dataset of datasets, each containing
    elements of one of the shards -- and return a dataset of elements. For
    example, the order of shards can be shuffled when loading them as follows:

    ```python
    def custom_reader_func(datasets):
      datasets = datasets.shuffle(NUM_SHARDS)
      return datasets.interleave(lambda x: x, num_parallel_calls=AUTOTUNE)

    dataset = tf.data.Dataset.load(
        path="/path/to/data", ..., reader_func=custom_reader_func)
    ```

    Args:
      path: Required. A path pointing to a previously saved dataset.
      element_spec: Optional. A nested structure of `tf.TypeSpec` objects
        matching the structure of an element of the saved dataset and specifying
        the type of individual element components. If not provided, the nested
        structure of `tf.TypeSpec` saved with the saved dataset is used. Note
        that this argument is required in graph mode.
      compression: Optional. The algorithm to use to decompress the data when
        reading it. Supported options are `GZIP` and `NONE`. Defaults to `NONE`.
      reader_func: Optional. A function to control how to read data from shards.
        If present, the function will be traced and executed as graph
        computation.

    Returns:
      A `tf.data.Dataset` instance.

    Raises:
      FileNotFoundError: If `element_spec` is not specified and the saved nested
        structure of `tf.TypeSpec` can not be located with the saved dataset.
      ValueError: If `element_spec` is not specified and the method is executed
        in graph mode.
    """
# Loaded lazily due to a circular dependency (dataset_ops -> load_op ->
# dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import load_op
exit(load_op._load(
    path=path,
    element_spec=element_spec,
    compression=compression,
    reader_func=reader_func))
