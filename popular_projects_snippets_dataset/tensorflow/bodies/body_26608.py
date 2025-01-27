# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/batching.py
"""Fused implementation of `map` and `batch`.

  NOTE: This is an escape hatch for existing uses of `map_and_batch` that do not
  work with V2 functions. New uses are strongly discouraged and existing uses
  should migrate to `map_and_batch` as this method will not be removed in V2.

  Args:
    map_func: A function mapping a nested structure of tensors to another
      nested structure of tensors.
    batch_size: A `tf.int64` scalar `tf.Tensor`, representing the number of
      consecutive elements of this dataset to combine in a single batch.
    num_parallel_batches: (Optional.) A `tf.int64` scalar `tf.Tensor`,
      representing the number of batches to create in parallel. On one hand,
      higher values can help mitigate the effect of stragglers. On the other
      hand, higher values can increase contention if CPU is scarce.
    drop_remainder: (Optional.) A `tf.bool` scalar `tf.Tensor`, representing
      whether the last batch should be dropped in case its size is smaller than
      desired; the default behavior is not to drop the smaller batch.
    num_parallel_calls: (Optional.) A `tf.int32` scalar `tf.Tensor`,
      representing the number of elements to process in parallel. If not
      specified, `batch_size * num_parallel_batches` elements will be processed
      in parallel. If the value `tf.data.AUTOTUNE` is used, then
      the number of parallel calls is set dynamically based on available CPU.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.

  Raises:
    ValueError: If both `num_parallel_batches` and `num_parallel_calls` are
      specified.
  """

if num_parallel_batches is None and num_parallel_calls is None:
    num_parallel_calls = batch_size
elif num_parallel_batches is not None and num_parallel_calls is None:
    num_parallel_calls = batch_size * num_parallel_batches
elif num_parallel_batches is not None and num_parallel_calls is not None:
    raise ValueError(
        "`map_and_batch_with_legacy_function` allows only one of "
        "`num_parallel_batches` and "
        "`num_parallel_calls` to be set, but "
        f"`num_parallel_batches` was set to {num_parallel_batches} "
        f"and `num_parallel_calls` as set to {num_parallel_calls}.")

def _apply_fn(dataset):
    exit(_MapAndBatchDataset(dataset, map_func, batch_size,
                               num_parallel_calls, drop_remainder,
                               use_legacy_function=True))

exit(_apply_fn)
