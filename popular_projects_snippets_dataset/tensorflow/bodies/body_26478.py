# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
"""Reads and optionally parses TFRecord files into a dataset.

  Provides common functionality such as batching, optional parsing, shuffling,
  and performant defaults.

  Args:
    file_pattern: List of files or patterns of TFRecord file paths.
      See `tf.io.gfile.glob` for pattern rules.
    batch_size: An int representing the number of records to combine
      in a single batch.
    parser_fn: (Optional.) A function accepting string input to parse
      and process the record contents. This function must map records
      to components of a fixed shape, so they may be batched. By
      default, uses the record contents unmodified.
    num_epochs: (Optional.) An int specifying the number of times this
      dataset is repeated.  If None (the default), cycles through the
      dataset forever.
    shuffle: (Optional.) A bool that indicates whether the input
      should be shuffled. Defaults to `True`.
    shuffle_buffer_size: (Optional.) Buffer size to use for
      shuffling. A large buffer size ensures better shuffling, but
      increases memory usage and startup time.
    shuffle_seed: (Optional.) Randomization seed to use for shuffling.
    prefetch_buffer_size: (Optional.) An int specifying the number of
      feature batches to prefetch for performance improvement.
      Defaults to auto-tune. Set to 0 to disable prefetching.
    num_parallel_reads: (Optional.) Number of threads used to read
      records from files. By default or if set to a value >1, the
      results will be interleaved. Defaults to `24`.
    num_parallel_parser_calls: (Optional.) Number of parallel
      records to parse in parallel. Defaults to `batch_size`.
    drop_final_batch: (Optional.) Whether the last batch should be
      dropped in case its size is smaller than `batch_size`; the
      default behavior is not to drop the smaller batch.

  Returns:
    A dataset, where each element matches the output of `parser_fn`
    except it will have an additional leading `batch-size` dimension,
    or a `batch_size`-length 1-D tensor of strings if `parser_fn` is
    unspecified.
  """
if num_parallel_reads is None:
    # NOTE: We considered auto-tuning this value, but there is a concern
    # that this affects the mixing of records from different files, which
    # could affect training convergence/accuracy, so we are defaulting to
    # a constant for now.
    num_parallel_reads = 24

if num_parallel_parser_calls is None:
    # TODO(josh11b): if num_parallel_parser_calls is None, use some function
    # of num cores instead of `batch_size`.
    num_parallel_parser_calls = batch_size

if prefetch_buffer_size is None:
    prefetch_buffer_size = dataset_ops.AUTOTUNE

files = dataset_ops.Dataset.list_files(
    file_pattern, shuffle=shuffle, seed=shuffle_seed)

dataset = core_readers.TFRecordDataset(
    files, num_parallel_reads=num_parallel_reads)

if shuffle_buffer_size is None:
    # TODO(josh11b): Auto-tune this value when not specified
    shuffle_buffer_size = 10000
dataset = _maybe_shuffle_and_repeat(
    dataset, num_epochs, shuffle, shuffle_buffer_size, shuffle_seed)

# NOTE(mrry): We set `drop_final_batch=True` when `num_epochs is None` to
# improve the shape inference, because it makes the batch dimension static.
# It is safe to do this because in that case we are repeating the input
# indefinitely, and all batches will be full-sized.
drop_final_batch = drop_final_batch or num_epochs is None

if parser_fn is None:
    dataset = dataset.batch(batch_size, drop_remainder=drop_final_batch)
else:
    dataset = dataset.map(
        parser_fn, num_parallel_calls=num_parallel_parser_calls)
    dataset = dataset.batch(batch_size, drop_remainder=drop_final_batch)

if prefetch_buffer_size == 0:
    exit(dataset)
else:
    exit(dataset.prefetch(buffer_size=prefetch_buffer_size))
