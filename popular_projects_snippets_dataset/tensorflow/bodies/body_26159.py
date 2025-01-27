# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Samples elements at random from the datasets in `datasets`.

    Creates a dataset by interleaving elements of `datasets` with `weight[i]`
    probability of picking an element from dataset `i`. Sampling is done without
    replacement. For example, suppose we have 2 datasets:

    ```python
    dataset1 = tf.data.Dataset.range(0, 3)
    dataset2 = tf.data.Dataset.range(100, 103)
    ```

    Suppose that we sample from these 2 datasets with the following weights:

    ```python
    sample_dataset = tf.data.Dataset.sample_from_datasets(
        [dataset1, dataset2], weights=[0.5, 0.5])
    ```

    One possible outcome of elements in sample_dataset is:

    ```
    print(list(sample_dataset.as_numpy_iterator()))
    # [100, 0, 1, 101, 2, 102]
    ```

    Args:
      datasets: A non-empty list of `tf.data.Dataset` objects with compatible
        structure.
      weights: (Optional.) A list or Tensor of `len(datasets)` floating-point
        values where `weights[i]` represents the probability to sample from
        `datasets[i]`, or a `tf.data.Dataset` object where each element is such
        a list. Defaults to a uniform distribution across `datasets`.
      seed: (Optional.) A `tf.int64` scalar `tf.Tensor`, representing the random
        seed that will be used to create the distribution. See
        `tf.random.set_seed` for behavior.
      stop_on_empty_dataset: If `True`, sampling stops if it encounters an empty
        dataset. If `False`, it continues sampling and skips any empty datasets.
        It is recommended to set it to `True`. Otherwise, the distribution of
        samples starts off as the user intends, but may change as input datasets
        become empty. This can be difficult to detect since the dataset starts
        off looking correct. Default to `False` for backward compatibility.
      rerandomize_each_iteration: An optional `bool`. The boolean argument
      controls whether the sequence of random numbers used to determine which
      dataset to sample from will be rerandomized each epoch. That is, it
      determinies whether datasets will be sampled in the same order across
      different epochs (the default behavior) or not.

    Returns:
      A dataset that interleaves elements from `datasets` at random, according
      to `weights` if provided, otherwise with uniform probability.

    Raises:
      TypeError: If the `datasets` or `weights` arguments have the wrong type.
      ValueError:
        - If `datasets` is empty, or
        - If `weights` is specified and does not match the length of `datasets`.
    """
# Loaded lazily due to a circular dependency
# (dataset_ops -> sample_from_datasets_op -> dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import sample_from_datasets_op
exit(sample_from_datasets_op._sample_from_datasets(  # pylint: disable=protected-access
    datasets,
    weights,
    seed,
    stop_on_empty_dataset,
    rerandomize_each_iteration,
))
